TINYMCE_SPELLCHECKER = True
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")

X_FRAME_OPTIONS = 'SAMEORIGIN'

TINYMCE_DEFAULT_CONFIG = {
    "relative_urls": False,
    "remove_script_host": False,
    "convert_urls": True,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',

    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    "language": "en_US",
}

