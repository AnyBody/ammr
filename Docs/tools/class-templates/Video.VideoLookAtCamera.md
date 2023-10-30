(Video.VideoLookAtCamera.any)=
# VideoLookAtCamera

Creates a video object for saving mp4 videos from model simulations

:Usage: 
    Add the following to your model to use the class templates in the file
    ```{code-block} AnyScriptDoc
    #include "<ANYBODY_PATH_MODELUTILS>/Video/VideoLookAtCamera.any"`
    ``` 



(Video.VideoLookAtCamera.VideoLookAtCamera)=

## VideoLookAtCamera

```{code-block} AnyScriptDoc
VideoLookAtCamera <ObjectName>() = {};
```

:class type: `AnyFolder`
:Optional args:
  
    - `UP_DIRECTION = y`
    - `CREATE_GIF = 0`
    - `_AUTO_PLAY_VIDEOS = 1`
    - `_OVER_WRITE = 1`
    - `_DEBUG = 0`
    - `_CLEAN_UP_IMAGES = 1`
    - `_AUTO_OPEN_PREVIEW_ = 1`
    - `ENABLE_SAVE_SETTINGS = 0`
    - `ENABLE_OVERLAY = 1`


Add `#include "<ANYBODY_PATH_MODELUTILS>/Video/VideoLookAtCamera.any".
Then use the class template to create a video object:

**EXAMPLE:**
```
  #include "<ANYBODY_PATH_MODELUTILS>/Video/VideoLookAtCamera.any"

  // This is a simple example of using the camera class to create videos.
  VideoLookAtCamera MyCam (UP_DIRECTION = y) = 
  {
       // The point the camera focus on  
       CameraLookAtPoint = Main.MyModel.Femur.Knee.r;  

       // The vertical field of view in meters at the LookAtPoint
       CameraFieldOfView = 1;

       // The direction which the camera is placed
       // (In global coordinates with respect to the LookAtPoint)
       CameraDirection = {1, 1, -1};

       // The operations which should be included in the video.
       Analysis = {
           AnyOperation &ref = Main.MyStudy.InverseDynamics;
       };
   };
```
TO CREATE A VIDEO RUN THE FOLLOWING OPERATION:
    Main.MyCam.Create_Video


