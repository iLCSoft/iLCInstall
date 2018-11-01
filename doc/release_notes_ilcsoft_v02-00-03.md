## LCFIPlus v00-07

* 2018-10-30 Ryo Yonamine ([PR#45](https://github.com/lcfiplus/LCFIPlus/pull/45))
  - Add initializatioin.
  - Prevent accessing a null pointer.

* 2018-10-22 Ryo Yonamine ([PR#44](https://github.com/lcfiplus/LCFIPlus/pull/44))
  - bug fix. "1" and "0" didn't work after the previous modification. now any of "true", "false", "1", "0" work.

* 2018-10-19 Ryo Yonamine ([PR#43](https://github.com/lcfiplus/LCFIPlus/pull/43))
  - too-small primary vertex postion errrors
  - problems caused due to the ip semaring
  - problem with which boolean parameters were not able to set by "true" or "false"
  
  New variables for flavor tagging introduced :(d0/z0)prob(b/c/q)2.
  These can be used istead of (d0/z0)prob(b/c/q).
  This fixs the problem that maximax exceeds 1.
  The flavor tagging performance will be slightly improved.

