# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:56:39 2018

@author: poduval
"""

import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

conda install -c conda-forge jupyter_contrib_nbextensions jupyter_nbextensions_configurator

