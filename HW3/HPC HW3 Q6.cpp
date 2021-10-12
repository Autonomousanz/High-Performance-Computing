
#include <iostream>
#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
using namespace std;
using namespace cv;
int delayTime = 1500;
int delayBlur = 100;
int MAX_KERNEL_LENGTH = 31;
Mat src; Mat dst;
char window_name[] = "Smoothing Demo";
int displayText(const char* caption);
int displayPicture(int delay);
int main(int argc, char** argv)
{
    namedWindow(window_name, WINDOW_AUTOSIZE);
    const char* filename = argc >= 2 ? argv[1] : "C:/Users/sansk/OneDrive/Desktop/college assignments/nature.jpg";
    src = imread(samples::findFile(filename), IMREAD_COLOR);
    if (src.empty())
    {
        printf(" Error opening image\n");
        printf(" Usage:\n %s [image_name-- default MyPic.jpg] \n", argv[0]);
        return EXIT_FAILURE;
    }
    if (displayText("Original Image") != 0)
    {
        return 0;
    }
    dst = src.clone();
    if (displayPicture(delayTime) != 0)
    {
        return 0;
    }
   
    if (displayText("Bilateral Blur") != 0)
    {
        return 0;
    }
    for (int i = 1; i < MAX_KERNEL_LENGTH; i = i + 2)
    {
        bilateralFilter(src, dst, i, i * 2, i / 2);
        if (displayPicture(delayBlur) != 0)
        {
            return 0;
        }
    }    
    return 0;
}
int displayText(const char* caption)
{
    dst = Mat::zeros(src.size(), src.type());
    putText(dst, caption,
        Point(src.cols / 4, src.rows / 2),
        FONT_HERSHEY_COMPLEX, 1, Scalar(255, 255, 255));
    return displayPicture(delayTime);
}
int displayPicture(int delay)
{
    imshow(window_name, dst);
    int c = waitKey(delay);
    if (c >= 0) { return -1; }
    return 0;
}