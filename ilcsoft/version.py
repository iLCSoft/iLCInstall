##################################################
# Version class
# Author: Jan Engels, DESY
# Date: Jun, 2008
##################################################

import os
import operator
import string
import re
from functools import reduce

__all__ = [ 'Version' ]

class Version:
    """ helper class for comparing versions.
        internally creates a tuple with the version from
        a string (or a sequence) passed to the constructor
        which is then used for comparisons.



        examples of valid versions and their
        internal tuple representation:

        Version( 'v01-03-03' )  -> (1,3,3)
        Version( '2.0.3.1' )    -> (2,0,3,1)
        Version( '1.3.0.0' )    -> (1,3)        # trailing zeros are removed
        Version( [1,0,0] )      -> (1,)         # trailing zeros are removed
        Version( 'HEAD' )       -> ('HEAD',)
        
        HEAD version is greater than any other version, e.g.:

        Version( 'HEAD' ) > '1.2' == True
        'head' > Version( '1.2' ) == True


        a version can also be extracted from a command output
        Version( commands.getoutput( 'java -version') )

        a list of all versions found is also available:
        Version( commands.getoutput( 'qmake -v') ).versions[-1]

        version objects have a string representation dependent on the constructor
        argument and parameters, i.e.:

        str( Version( 'v01-03-04' ))    == 'v01-03-04'
        str( Version( [1, 3, 4] ))      == '1.3.4'
        str( Version( (1, 3, 4) ))      == '1.3.4'
        str( Version( 'v01-03-04', strict=True ))   == '1.3.4'

        the strict option forces the version string representation to a dot-separated
        string of elements xx.yy.zz

        versions can be sliced and individual elements can be returned:
        Version( 'v01-03-04' )[:2] == (1,3)
        Version( 'v01-03-04' )[0] == 1

        defining max_elements allows you to cut off elements, e.g.:

        Version( '1.5.2-3', max_elements=3 ) == (1,5,2) # cuts off exceeding elements

        Note: using the max_elements restriction forces strict mode to True, i.e.:
        str( Version( 'v01-03-04-patch3', max_elements=3 )) == '1.3.4'
    """
    _min_elements = 2
    _separators = '-_,.'

    # regular expression for checking if a string contains a version
    # a version has to have at least min elements separated by one version_separator
    # the end slice removes the last separators
    _regex = (_min_elements * ('\d+ [%s] ' % _separators))[:-(4+len(_separators))]
    _re_has_version = re.compile( _regex, re.VERBOSE )

    # regular expression for extracting all digits in a string
    _re_any_digit = re.compile( '(\d+)' )

    def __init__(self, arg, max_elements=None, strict=False):

        # store a list of all versions in a list (including this object itself!)
        self.versions = [self]

        # strings require some work...
        if isinstance(arg, str):

            # strip white spaces
            arg = arg.strip()

            # head version is a special case
            if arg.upper() == 'HEAD':
                self._strver = arg
                self._cmpver = self._repver = (arg.upper(),)
                return

            # split by newlines
            ver = arg.split( os.linesep )

            # filter out lines without versions
            ver = [ i for i in ver if self._re_has_version.search(i) ]

            # split by whitespaces
            ver = list(map( str.split, ver ))

            # filter out elements without version(s) and merge them into single list
            ver = [ j for i in ver for j in i if self._re_has_version.search(j) ]

            # split by os.sep (in case of a path)
            ver = [x.split( os.sep ) for x in ver]

            # filter out elements without version(s) and merge elements into single list
            ver = [ j for i in ver for j in i if self._re_has_version.search(j) ]

            # strip leading/trailing garbage characters
            ver = [ i.strip( string.punctuation ) for i in ver ]

            if len(ver) == 0:
                raise ValueError('invalid version string "%s": no versions were found' % arg)

            # create this object with the first element
            strver = ver.pop(0)
            intver = self._re_any_digit.findall( strver )
            self._cmpver, self._repver, self._strver = self._validate( intver, max_elements )

            # take the loose string representation if no restrictions are set
            if not strict and max_elements == None:
                self._strver = strver

            # if more than one version was found go through the rest
            for v in ver:
                try:
                    # call the constructor for each version
                    new = self.__class__(v, max_elements, strict)
                except ValueError:
                    pass
                else:
                    # remove duplicates
                    if not new in self.versions:
                        self.versions.append( new )

            return

        self._cmpver, self._repver, self._strver = self._validate( arg, max_elements )

    def _validate(self, arg, max_elements=None):
        """ returns a valid version tuple according to following criterias:
                - argument must be a sequence
                - elements must be integers or convertible to int
                - at least one element must be greater than 0
                - if max_elements != None cut off exceeding elements
            a ValueError is raised if an error occurs
        """

        # HEAD version is a special case
        if arg == ('HEAD',):
            return (arg, 'HEAD', 'HEAD')

        # check if arg is a sequence
        #if not ( '__len__' in dir(arg) and '__getitem__' in dir(arg) ):
        #    raise ValueError, 'invalid version "%s": is not a sequence' % (arg,)

        # check if arg is a sequence
        try:
            ver = list(arg)
        except:
            raise ValueError('invalid version "%s": is not a sequence' % (arg,))

        # check max elements
        if max_elements != None and len(ver) > max_elements:
            ver = ver[:max_elements]

        # cast elements to integers
        try:
            ver = [ int(i) for i in ver if i != None and i != '' ]
        except:
            raise ValueError('invalid version "%s: element cannot be cast to integer"' % (arg,))
        
        # version numbers must be >= 0
        if min(ver) < 0:
            raise ValueError('invalid version "%s": version numbers must be >=0' % (arg,))

        # at least one element must be greater than 0
        if reduce( operator.add, ver ) <= 0:
            raise ValueError('invalid version "%s": at least one element must be greater than 0' % (arg,))

        # remove exceeding 0's at the end, so 1.3.0.0 == 1.3.0 == 1.3
        cmpver = ver[:]
        while cmpver[-1] == 0: cmpver.pop()

        # fill with 0' until min_elements is reached
        repver = ver + (self._min_elements-len(ver))*[0]

        strver = str.join('.', list(map(str, repver)))

        return (tuple(cmpver),tuple(repver), strver)

    def __getitem__(self, n):
        return self._repver[n]

    def __getslice__(self, i, j):
        i = max(i, 0); j = max(j, 0)
        return self._repver[i:j]

    def __len__(self):
        return len(self._repver)

    def __repr__(self):
        return repr(self._strver)

    def __str__(self):
        return self._strver

    def __cmp__(self, other):
        #print 'cmp - self:', self, 'other:', other
        #if other:
        #    if isinstance( other, self.__class__ ):
        #        return cmp(self._cmpver, other._cmpver )
        #    #print 'cmp - converting other:', other
        #    return cmp(self._cmpver, self.__class__(other)._cmpver)

        if other:
            #print 'cmp - converting other:', other
            return cmp(self._cmpver, self.__class__(other)._cmpver)

        return cmp(self._cmpver, other)


if __name__ == '__main__':
    v0=Version( 'head' )
    v1=Version( 'v01-03-03' )
    v2=Version( 'v01-03-03', strict=True )
    v3=Version( 'v01-03-03', max_elements=2 )
    v4=Version( list(range(4)) )
    v5=Version( list(range(4)), max_elements=3 )
    import os.path
    ilcHome='/afs/desy.de/group/it/ilcsoft/'
    if os.path.isdir( ilcHome ):
        from subprocess import getoutput
        c1=Version( getoutput( ilcHome+'CMake/2.4.6/bin/cmake --version' ).replace('patch ',''))
        q1=Version( getoutput( 'qmake -v' ), strict=True)
        q2=Version( getoutput( ilcHome+'QT/4.2.2/bin/qmake -v' ))
        #j1=Version( getoutput( ilcHome+'java/1.5.0/bin/java -version' ))
        #j2=Version( getoutput( ilcHome+'java/1.5.0/bin/java -version' ), max_elements=3, strict=True)

