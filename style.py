from IPython.core.display import HTML

def set_css_style(css_file_path):
   """
   Read the custom CSS file and load it into Jupyter.
   Pass the file path to the CSS file.
   """

   styles = open(css_file_path, "r").read()
   s = '<style type="text/css">%s</style>' % styles     
   return HTML(s)
set_css_style("custom.css")