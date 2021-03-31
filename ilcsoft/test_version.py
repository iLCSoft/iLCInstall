################################################
# py.test module for testing the Version class
################################################

from .version import Version
import py

def test_sanity():
    py.test.raises(TypeError, Version )
    py.test.raises(ValueError, Version, 0)
    py.test.raises(ValueError, Version, [])
    py.test.raises(ValueError, Version, '')
    py.test.raises(ValueError, Version, '1')
    py.test.raises(ValueError, Version, '1.')
    py.test.raises(ValueError, Version, 'a.b')
    py.test.raises(ValueError, Version, 'blah')

def test_general():

    MIN_ELEM = Version._min_elements

    # versions must have at least one element > 0
    py.test.raises(ValueError, Version, MIN_ELEM * (0,) )

    # elements must be integers or convertible to int
    py.test.raises(ValueError, Version, (MIN_ELEM * [1]) + ['a'] )

    # elements must be >= 0
    py.test.raises(ValueError, Version, (MIN_ELEM * [1]) + [-1] )

    # cutting off / filling missing elements
    MAX_ELEM = 4
    assert Version( (MAX_ELEM + 1) * (1,) , max_elements = MAX_ELEM ) == MAX_ELEM * (1,)
    assert Version( (MAX_ELEM + 1) * '1.' , max_elements = MAX_ELEM ) == MAX_ELEM * (1,)

    # getitem / getslice
    NUM_ELEM = MIN_ELEM+2
    assert Version( list(range(NUM_ELEM)) )[NUM_ELEM-1] == NUM_ELEM-1
    assert Version( list(range(NUM_ELEM)) )[1:NUM_ELEM-1] == tuple(range(1,NUM_ELEM-1))

    # strict vs non-strict
    assert str( Version( (NUM_ELEM * '1.')+'1-01' )) == (NUM_ELEM * '1.')+'1-01'
    assert str( Version( (NUM_ELEM * '1.')+'1-01', strict=True )) == (NUM_ELEM * '1.')+'1.1'

    # None, [], '' comparisons
    assert Version('HEAD') != None
    assert Version('HEAD') != []
    assert Version('HEAD') != ''

def test_eq():

    eq = [
        ( (2,2,3,1) , (2,2,3,1) ),
        ( [2,2,3,1] , [2,2,3,1] ),
        ( '2.2.3.1' , '2.2.3.1' ),

        ( (2,2,3,1) , [2,2,3,1] ),
        ( (2,2,3,1) , '2.2.3.1' ),
        ( [2,2,3,1] , '2.2.3.1' ),

        ( (1,1)     , [1,1,0,0] ),
        ( (1,1)     , '1.1.0.0' ),
        ( '1.1'     , '1.1.0.0' ),
        ( '1.1'     , '1.1.0.'  ),
        ( '1.1'     , '1.1.0'   ),
        
        ( 'v01-02'  , (1,2,0,0) ),
        ( '1.2-3_4' , (1,2,3,4) ),
        
        ( 'HEAD'    , 'HEAD'    ),
        ( 'head'    , 'Head'    ),
    ]

    for case in eq:
        assert Version(case[0]) == Version(case[1]), 'Version(%s) should equal Version(%s)' % case
        assert Version(case[0]) == case[1], 'Version(%s) should equal %s' % case
        assert case[0] == Version(case[1]), '%s should equal Version(%s)' % case


def test_ne():

    ne = [
        ( (2,2,3,1) , (2,2,3,2) ),
        ( [2,2,3,1] , [2,2,3,2] ),
        ( '2.2.3.1' , '2.2.3.2' ),

        ( (2,2,3,1) , [2,2,3,2] ),
        ( (2,2,3,1) , '2.2.3.2' ),
        ( [2,2,3,1] , '2.2.3.2' ),

        ( (1,1)     , [1,2,0,0] ),
        ( (1,1)     , '1.2.0.0' ),
        ( '1.1'     , '1.2.0.0' ),
        ( '1.1'     , '1.2.0.'  ),
        ( '1.1'     , '1.2.0'   ),
        
        ( 'v01-02'  , (1,3,0,0) ),
        ( '1.2.3-4' , (1,2,3,5) ),
        
        ( 'head'    , (1,2,3,4) ),
        ( 'head'    , [1,2,3,4] ),
        ( 'head'    , '1.2.3.4' ),
    ]

    for case in ne:
        assert Version(case[0]) != Version(case[1]), 'Version(%s) should not equal Version(%s)' % case
        assert Version(case[0]) != case[1], 'Version(%s) should not equal %s' % case
        assert case[0] != Version(case[1]), '%s should not equal Version(%s)' % case


def test_lt_gt():

    lt_gt = [
        ( (2,2,3,1) , (2,2,3,2) ),
        ( [2,2,3,1] , [2,2,3,2] ),
        ( '2.2.3.1' , '2.2.3.2' ),

        ( (2,2,3,1) , [2,3,4,2] ),
        ( (2,2,3,1) , '2.3.4.2' ),
        ( [2,2,3,1] , '2.3.4.2' ),

        ( (0,9)     , [1,0,0,0] ),
        ( (0,9)     , '1.0.0.0' ),
        ( '0.9'     , '1.0.0.0' ),
        ( '0.9'     , '1.0.0.'  ),
        ( '0.9'     , '1.0.0'   ),
        
        ( 'v01-02'  , (1,3,0,0) ),
        ( '1.2.3-4' , (1,2,3,5) ),
        ( '0.9.9.9' , (1,0,0)   ),
        ( '0.0.9.9' , (0,1,0)   ),
        ( '0.0.0.9' , (0,0,1)   ),
        
        ( (1,2,3,4) , 'head'    ),
        ( [1,2,3,4] , 'head'    ),
        ( '1.2.3.4' , 'head'    ),
    ]

    for case in lt_gt:
        
        # less than
        assert Version(case[0]) < Version(case[1]), 'Version(%s) should be less than Version(%s)' % case
        assert Version(case[0]) < case[1], 'Version(%s) should be less than %s' % case
        # Not really easy to support this direction in python3!
        # assert case[0] < Version(case[1]), '%s should be less than Version(%s)' % case

        # greater than
        assert Version(case[1]) > Version(case[0]), 'Version(%s) should be greater than Version(%s)' % (case[1], case[0])
        assert Version(case[1]) > case[0], 'Version(%s) should be greater than %s' % (case[1], case[0])
        # Not really easy to support this direction in python3!
        # assert case[1] > Version(case[0]), '%s should be greater than Version(%s)' % case


def test_cmd_outputs():
    from .util import OSDetect
    
    sl_ver = OSDetect().isSL()

    if sl_ver:
        import os.path
        from subprocess import getoutput
        
        ilcHome='/afs/desy.de/group/it/ilcsoft/'
        prdHome='/opt/products/'

        if os.path.isdir( ilcHome ):

            Version( getoutput( ilcHome + 'CMake/2.4.6/bin/cmake --version' ).replace('patch ','')) == '2.4.6'
            Version( getoutput( ilcHome + 'QT/4.2.2/bin/qmake -v' )).versions[-1] == '4.2.2'

            if sl_ver[0] == 3:
                assert Version( getoutput( ilcHome+'java/1.5.0/bin/java -version' ) , max_elements = 3) == '1.5.0'
                assert Version( getoutput( ilcHome+'java/1.5.0/bin/java -version' ) )[:3] == Version('1.5.0')
                assert Version( getoutput( '/usr/bin/qmake -v' ) ).versions[-1] == '3.1.2'
                assert Version( getoutput( 'java -version' ) ) == Version('1.4.2.15')
                assert Version( getoutput( 'java -version' ) )[:3] == Version('1.4.2')
                assert Version( getoutput( 'java -version' ) , max_elements = 3) == '1.4.2'

            if sl_ver[0] == 4:
                assert Version( getoutput( ilcHome+'java/1.6.0/bin/java -version' )) == '1.6.0.04'
                assert Version( getoutput( ilcHome+'java/1.6.0/bin/java -version' ) , max_elements = 3) == '1.6.0'
                assert Version( getoutput( ilcHome+'java/1.6.0/bin/java -version' ) )[:3] == Version('1.6.0')
                assert Version( getoutput( '/usr/bin/qmake -v' ) ).versions[-1] == '3.3.3'
                assert Version( getoutput( 'java -version' ) ) == Version('1.5.0.14')
                assert Version( getoutput( 'java -version' ) )[:3] == Version('1.5.0')
                assert Version( getoutput( 'java -version' ) , max_elements = 3) == '1.5.0'

        if os.path.isdir( prdHome ):

            assert Version( getoutput( prdHome+'java/1.4.2/bin/java -version' ), max_elements = 3) == '1.4.2'
            assert Version( getoutput( prdHome+'java/1.4.2/bin/java -version' ))[:3] == Version('1.4.2')

            if sl_ver[0] == 3:
                assert Version( getoutput( prdHome+'java/1.4.2/bin/java -version' )) == '1.4.2.15'
            if sl_ver[0] == 4:
                assert Version( getoutput( prdHome+'java/1.4.2/bin/java -version' )) == '1.4.2.16'


