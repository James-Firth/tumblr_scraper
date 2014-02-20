tumblr_scraper
==============

This python script currently grabs the images created by the tumblr user "posterology" in their series of Breaking Bad posters (one for every episode). They are downloaded and named with the alt-text of each image, and it removes any special accent characters such as 'é' and replaces it with the equivalent 'e'.

## To Modify

Change line 4 to contain whatever pages you want and line 6 to be the webpage you want. It also only currently downloads jpgs, this can also be changed on line 14.

## Requirements
* Python 2.7
* Beautiful Soup 4

## To Run
`python tumblr_scraper.py` will download all the images in the current directory.

## Misc

* Don't understand licenses? Check out [TL;DR Legal](https://tldrlegal.com/license/mit-license)
* Please let me know if you use this!


## License

The MIT License (MIT)

Copyright (c) 2014 James Firth

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
