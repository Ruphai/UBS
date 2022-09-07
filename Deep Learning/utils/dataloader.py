from torch.utils.data import Dataset
from PIL import Image

class OilPalmDataset(Dataset):
    """ DataSet class to read in images, transform their pixel values, and 
    stores the image tensors and labels
    """

    def __init__(
        self,
        dataframe,
        img_dir,
        transform=None):

        """
        Instantiate the OilPalmDataset class.
        
        Args:
            dataframe (pd.DataFrame): a dataframe with a row for each image and 
            column for img_id with a path to the TIF files.

            img_dir (pd.DataFrame): a dataframe with a path to the train dataset
            transform (list, optional): a list of transforms to apply to the feature data such as flipping
        Dataset ([inherit from the Dataset module]): [PyTorch Dataset object]
        """

        self.data = dataframe
        self.img_dir = img_dir
        self.transform = transform
        self.labels = self.data['has_oilpalm']

        # # Images
        self.images =self.data['img_id']
        #classes
        self.classes = set(self.labels)
        # Number of classes
        self.num_classes = len(self.classes)
        

    def __len__(self):
        return len(self.data)
        
    def __getitem__(self, idx):
        img_path = self.images.iloc[idx]

        # Open image from the image path provided
        img = Image.open(img_path)
        
        # Apply transformation on the image tensors
        if self.transform:
            img = self.transform(img)
        # Load the labels associated with the images
        label = self.labels.iloc[idx]
        
        return img, label
