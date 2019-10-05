# Face Detection using DLIB in Raspberry Pi

Simple code in python using DLIB for Face Detection in Raspberry Pi or any other PC.

## Dependencies

1. Python 3
2. opencv (tested with 3.4) #Watch https://youtu.be/xlmJsTeZL3w this video for opencv installation in Raspberry Pi
3. dlib	(tested with 19.18.0)
4. imutils (tested with 0.5.3) #sudo pip install imutils

## Run 

```
Python3 face_detect.py
```

## Setups for Raspberry Pi

To use Raspberry Pi camera module

```
#c = VideoStream(src=0).start()         	//For webcam, comment it if using Raspberry Pi Camera module 
c = VideoStream(usePiCamera=True).start()       //For Raspberry Pi Camera module, comment it if using webcam
```

To use webcam

```
c = VideoStream(src=0).start()         		//For webcam
#c = VideoStream(usePiCamera=True).start()       //For Raspberry Pi Camera
```

## Setups for any other PC

To use default webcam
```
c = VideoStream(src=0).start()

```

To use external webcam
```
c = VideoStream(src=1).start() #If system has more than one webcam use the 'src' number accordingly

```

## Authors

**Arijit Das** 


## Acknowledgments

* https://www.pyimagesearch.com/



