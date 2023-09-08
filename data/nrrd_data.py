import numpy as np
import  nrrd #pynrrd
import nibabel as  nib
import matplotlib.pyplot as plt

# import matplotlib as mpl
# from PIL import  Image
# 
# def create_gif(data):
#     images = []
#     cmap = mpl.colormaps['coolwarm']
#     for i in range(data.shape[2]) :
#         image = Image.fromarray(data[:,:,i]).convert('L')
#         image =np.array(image)
#         image = cmap(image)
#         image = np.uint8(image*255)
#         images.append(Image.fromarray(image))
#      
#     images[0].save("ct.gif", format="GIF", append_images=images,save_all=True, duration=100, loop=0)   

if __name__ == '__main__' :
#     filename = '/mnt/hd-data/Datasets/med/liver/Lits/test/test-volume-0.nii'
#     img = nib. load(filename)
#     data = img.get_fdata()
    

         # Some sample numpy data
    filename = '/mnt/hd-data/Datasets/med/liver/CSM/image/csm_001_image.nrrd'
         
    data, header = nrrd.read(filename)
    # Read the data back from file
    # print(data.shape)
    maxv = np.max(data[:,:,0])
    minv = np.min(data[:,:,0])
    print('{} {}'.format(maxv, minv))
    print(data.dtype)
    for i in range(data.shape[2]) :
        plt.cla()
        plt.imshow(data[:,:, i], cmap = 'coolwarm')    
        plt.waitforbuttonpress(0.01)
    plt.show()
#         #create_gif(data)

