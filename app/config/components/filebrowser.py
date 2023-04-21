FILEBROWSER_DIRECTORY = ''
FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
}
FILEBROWSER_SELECT_FORMATS = {
    'file': ['Image', 'Document', 'Video', 'Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
}
FILEBROWSER_VERSIONS_BASEDIR = '_versions'
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 100, 'height': 100, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
}
FILEBROWSER_VERSION_QUALITY = 90
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big', 'large']
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'
FILEBROWSER_VERSION_PROCESSORS = [
    'filebrowser.utils.scale_and_crop',
]
FILEBROWSER_VERSION_NAMER = 'filebrowser.namers.VersionNamer'
FILEBROWSER_PLACEHOLDER = ""
FILEBROWSER_SHOW_PLACEHOLDER = False
FILEBROWSER_FORCE_PLACEHOLDER = False
FILEBROWSER_MAX_UPLOAD_SIZE = 128000000