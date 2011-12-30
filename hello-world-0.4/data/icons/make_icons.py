import os
import sys
import glob
import subprocess

theme_path = os.path.join(os.getcwd(), 'hicolor')
svg_path = os.path.join(theme_path, 'scalable')
if not os.path.exists(svg_path):
    sys.exit("Source directory does not exist: %s" % svg_path)    

icon_count = 0
for sub_folder in os.listdir(svg_path):
    source_path = os.path.join(svg_path, sub_folder)
    if not os.path.isdir(source_path):
        continue # skip files   
    print "Scanning '%s' folder..." % sub_folder
    
    for filename in glob.glob(os.path.join(source_path, "*.svg")):
        source_svg = os.path.join(source_path, filename)
        icon_name = os.path.basename(filename)[:-4]
        
        for size in [str(s) for s in (16,22,24,32,48,64,128)]:
            dimensions = "%sx%s" % (size, size)
            dest_path = os.path.join(theme_path, dimensions, sub_folder)
            if not os.path.exists(dest_path):
                print "Creating folder: " + dest_path
                os.makedirs(dest_path)
            dest_png = os.path.join(dest_path, icon_name + '.png')
            if not os.path.exists(dest_png):
                print "Creating icon: %s" % dest_png
                subprocess.call(["rsvg", "-w", size, "-h", size, source_svg, dest_png])
                icon_count += 1
print "Done. %s icons created." % icon_count

