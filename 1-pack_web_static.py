#!/usr/bin/python3

"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
Prototype: def do_pack():
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
    The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None
    """
    from os import path
    from datetime import datetime
    from fabric.api import local

if __name__ == "__main__":
        def do_pack():
    """
    function that generates a .tgz archive from the contents of the 
    web_static folder of your AirBnB Clone repo. it returns the archive
    path if the archive has been correctly generated. Otherwise, it should
    return None
    """
    date = datetime.utcnow()
    archive = f"versions/web_static_{date.year}{date.month}{date.day}{date.hour}{date.minute}{date.second}.tgz"
    if path.isdir("versions") is False:
    if local("mkdir -p versions").failed is True:
    return (None)
    if local(f"tar -cvzf {archive} web_static").failed is True:
    return (None)
    else:
    return (archive)
