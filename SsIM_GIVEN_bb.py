
def Ssim_Implementation(Ref_img,
                        Test_img,
                        X,
                        Y,
                        H,
                        W):
    str=""
#import the necessery packages
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    import skimage
    from skimage import data, img_as_float
    from skimage.measure import compare_ssim as ssim
    from PIL import Image, ImageEnhance
#Image Decleration
    Image_1 =  cv2.imread(Ref_img)
    Image_2 =  cv2.imread(Test_img)
    #cv2.destroyAllWindows()
#checking if bot the images have the same shape and size
    if Image_1.shape == Image_2.shape:
        print("shape and size of Ref image :", Image_1.shape, "and", Image_1.size)
        print("shape of size of  Test image:", Image_2.shape,"and", Image_2.size)
    else:
        print("Image shape and size differs")
        exit()
#Bounding Box decleration
    yint=int(Y)
    wint=int(W)
    xint=int(X)
    hint=int(H)
    a=yint+wint
    B=xint+hint
    bbox_Ref = Image_1[yint: a, xint: B]
    bbox_Test = Image_2[yint: a, xint:B]
    #bbox_Ref = Image_1[Y: Y+W, X: X+H]
    #bbox_Test = Image_2[Y: Y+W, X: X+H]

    print("The X-coordinate, Y-coordinate, Height and Width are : ", X, Y, H, W)
    # str="The X-coordinate, Y-coordinate, Height and Width are : "+X + Y + H + W
    print("The shape of Reference ROI and Test ROI:", bbox_Ref.shape,"and",bbox_Test.shape)
    # str=str+"The shape of Reference ROI and Test ROI:" + bbox_Ref.shape +"and" + bbox_Test.shape
#SSIM
    img1 = bbox_Ref
    img_1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    image_Ref = skimage.img_as_float(img_1)
    img2 = bbox_Test
    img_2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    image_test = skimage.img_as_float(img_2)
#defining MSE
    #def mse(x, y):
     #   return np.linalg.norm(x - y)
    #fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4), sharex=True, sharey=True)
    #ax = axes.ravel()
    #mse_none = mse(image_Ref, image_Ref)
    ssim_none = ssim(image_Ref, image_Ref, data_range=image_Ref.max() - image_test.min())
    #mse_test = mse(image_Ref, image_test)
    ssim_test = ssim(image_Ref, image_test, data_range=image_test.max() - image_test.min())
    ssim_test = round(ssim_test,3)
    print("SSIM with same image : %s \n SSIM with test image : %s " %(ssim_none,ssim_test))
   # str="SSIM with same image : %s \n SSIM with test image : %s " %(ssim_none,ssim_test)+"\n"
    str = "SSIM with Test image : %s " %(ssim_test)
    str = "SSIM  : %s " % (ssim_test)
    if ssim_test >= 0.95:
        #str=str+"The Images are same"
        print("The Images are same")
    elif ssim_test > 0.75 < 0.95:
        #str = str+"Almost similar"
        print("Almost similar")
    elif ssim_test > 0.50 <0.75:
        #str=str+"Maybe or Maynot "
        print("Maybe or Maynot ")
    elif ssim_test <= 0.50:
       # str=str+"The images are different"
        print("The images are different")
# plotting SSIM between images

    """label = 'SSIM: {:.2f}'
    ax[0].imshow(image_Ref, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[0].set_xlabel(label.format(ssim_none))
    ax[0].set_title('Original image')
    ax[1].imshow(image_test, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[1].set_xlabel(label.format(ssim_test))
    ax[1].set_title('Original With Test Image')
    plt.show()
#Displaying Images
    #cv2.imshow("Reference image" , Ref_img)
    #cv2.imshow("Test image" , Test_img)
    cv2.imshow("BB1" , bbox_Ref)
    cv2.imshow("BB2" , bbox_Test)
    cv2.waitKey()"""
    return ssim_test



# my_function('/home/gta/SambaProject/Lohith/image1ed.png','/home/gta/SambaProject/Lohith/original.jpg','12','110','557','143')