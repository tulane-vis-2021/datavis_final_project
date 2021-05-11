#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: nadim
"""

# importing packages

%matplotlib # necessary for IPython terminal

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#loading data

rg_3763302 = mpimg.imread('/Users/nadim/Documents/datavis/data_vis_project/s_03763302_thm.jpg')

mapping_file = pd.read_csv('/Users/nadim/Documents/datavis/data_vis_project/data_vis_mapping.csv', header = None)
mapping_file = np.matrix(mapping_file)
power_traces = pd.read_csv('/Users/nadim/Documents/datavis/data_vis_project/power_traces.csv', header = None)
power_traces = np.matrix(power_traces)

power_traces_averaged = pd.read_csv('/Users/nadim/Documents/datavis/data_vis_project/power_traces_averaged.csv', header = None)
power_traces_averaged = np.matrix(power_traces_averaged)

#%% DATA CLEANING

power_traces_averaged_dB = 10 * np.log10(power_traces_averaged) # convert radar power to dB

location_array = np.arange(mapping_file[0,3],mapping_file[0,6]) # pixel trace location in radargram
location_array = np.flip(location_array)

# define dielectric constants
dc_co2_ice = 2.1
dc_water_ice = 3.15
dc_permafrost = 4.5
dc_granite = 5
dc_seawater_ice = 6
dc_snow = 10
dc_shale = 12.5
dc_wet_sand = 25
dc_clay = 30
dc_water = 80

# per-pixel time conversion
t_px = 0.0375/(10**6)

#speed of light
c = 3e8 #m/s

# co2 ice conversion
d_br_collect_co2_ice = []

for i in range(0,len(power_traces_averaged_dB)):
    
    diff = float(location_array[0]-location_array[i])
        
    t = diff*t_px #microseconds converted to s

    d_br = t*c/(2*(dc_co2_ice**0.5))
    d_br_collect_co2_ice.append(d_br)    

# water ice conversion
d_br_collect_water_ice = []

for i in range(0,len(power_traces_averaged_dB)):
    
    diff2 = float(location_array[0]-location_array[i])
        
    t2 = diff2*t_px #microseconds converted to s

    d_br2 = t2*c/(2*(dc_water_ice**0.5))
    d_br_collect_water_ice.append(d_br2)
    
# seawater ice conversion
d_br_collect_seawater_ice = []

for i in range(0,len(power_traces_averaged_dB)):
    
    diff3 = float(location_array[0]-location_array[i])
        
    t3 = diff3*t_px #microseconds converted to s

    d_br3 = t3*c/(2*(dc_seawater_ice**0.5))
    d_br_collect_seawater_ice.append(d_br3)
    
#%% define plottable data

x = power_traces_averaged_dB;
y = np.array(d_br_collect_co2_ice);
y2 = np.array(d_br_collect_water_ice);
y3 = np.array(d_br_collect_seawater_ice);

#%% CLICK EVENT -- UPDATE PLOT

plt.ion() #necessary for IPython terminal

def onclick(event):
    if event.button == 1:
        plt.clf()
        plt.subplot(1,2,1)
        plt.vlines(mapping_file[0,2],mapping_file[0,3],mapping_file[0,6],colors='Red')
        plt.imshow(rg_3763302,'gray')
        plt.xlim([3200,3300])
        plt.ylim([1380,1700])
        plt.gca().invert_yaxis()
        plt.xlabel("pixel # (~460 meters/pixel)")
        plt.ylabel("pixel # (0.0375 microseconds/pixel)")
        
        plt.subplot(1,2,2)
        plt.plot(x,y,label=r'$\epsilon_r$ = 2.1 (CO2 ice)',linewidth=0.5,alpha=0.4,color='deepskyblue')
        plt.plot(x,y2,label=r'$\epsilon_r$ = 3.15 (water ice)',color='royalblue')
        plt.text(-25,500,'default/dblclick: CO2 ice',fontsize='x-small')
        plt.text(-25,600,'click: water ice',fontsize='x-small')
        plt.text(-25,700,'rtclick: seawater ice',fontsize='x-small')
        fig.suptitle("Permittivity-dependent ice thickness in radar sounding")

    elif event.button == 3:
        plt.clf()
        plt.subplot(1,2,1)
        plt.vlines(mapping_file[0,2],mapping_file[0,3],mapping_file[0,6],colors='Red')
        plt.imshow(rg_3763302,'gray')
        plt.xlim([3200,3300])
        plt.ylim([1380,1700])
        plt.gca().invert_yaxis()
        plt.xlabel("pixel # (~460 meters/pixel)")
        plt.ylabel("pixel # (0.0375 microseconds/pixel)")
        
        plt.subplot(1,2,2)
        plt.plot(x,y,label=r'$\epsilon_r$ = 2.1 (CO2 ice)',linewidth=0.5,alpha=0.4,color='deepskyblue')
        plt.plot(x,y2,label=r'$\epsilon_r$ = 3.15 (water ice)',linewidth=0.5,alpha=0.4,color='royalblue')
        plt.plot(x,y3,label=r'$\epsilon_r$ = 6.0 (seawater ice)',color='navy')
        plt.text(-25,500,'default/dblclick: CO2 ice',fontsize='x-small')
        plt.text(-25,600,'click: water ice',fontsize='x-small')
        plt.text(-25,700,'rtclick: seawater ice',fontsize='x-small')
        fig.suptitle("Permittivity-dependent ice thickness in radar sounding")

    plt.gca().invert_yaxis()
    plt.draw()
    plt.gca().legend()
    plt.xlabel("reflection power [dB]")
    plt.ylabel("depth [meters]")
    
    if event.dblclick == 1:
        plt.clf()
        plt.subplot(1,2,1)
        plt.vlines(mapping_file[0,2],mapping_file[0,3],mapping_file[0,6],colors='Red')
        plt.imshow(rg_3763302,'gray')
        plt.xlim([3200,3300])
        plt.ylim([1380,1700])
        plt.gca().invert_yaxis()
        plt.xlabel("pixel # (~460 meters/pixel)")
        plt.ylabel("pixel # (0.0375 microseconds/pixel)")
        
        plt.subplot(1,2,2)
        plt.plot(x,y,label=r'$\epsilon_r$ = 2.1 (CO2 ice)',color='deepskyblue')
        plt.gca().invert_yaxis()
        plt.gca().legend()
        plt.text(-25,500,'default/dblclick: CO2 ice',fontsize='x-small')
        plt.text(-25,600,'click: water ice',fontsize='x-small')
        plt.text(-25,700,'rtclick: seawater ice',fontsize='x-small')
        plt.xlabel("reflection power [dB]")
        plt.ylabel("depth [meters]")
        fig.suptitle("Permittivity-dependent ice thickness in radar sounding")
    
fig,ax=plt.subplots(1,2)
plt.subplot(1,2,1)
plt.vlines(mapping_file[0,2],mapping_file[0,3],mapping_file[0,6],colors='Red')
plt.imshow(rg_3763302,'gray')
plt.xlim([3200,3300])
plt.ylim([1380,1700])
plt.gca().invert_yaxis()
plt.xlabel("pixel # (~460 meters/pixel)")
plt.ylabel("pixel # (0.0375 microseconds/pixel)")

plt.subplot(1,2,2)
plt.plot(x,y,label=r'$\epsilon_r$ = 2.1 (CO2 ice)',color='deepskyblue')
fig.canvas.mpl_connect('button_press_event',onclick)
plt.gca().invert_yaxis()
plt.text(-25,500,'default/dblclick: CO2 ice',fontsize='x-small')
plt.text(-25,600,'click: water ice',fontsize='x-small')
plt.text(-25,700,'rtclick: seawater ice',fontsize='x-small')
plt.gca().legend()
plt.xlabel("reflection power [dB]")
plt.ylabel("depth [meters]")
fig.suptitle("Permittivity-dependent ice thickness in radar sounding")

fig.set_size_inches(8,8,forward=True)

#%% CURSOR SNAP

plt.ion() #necessary for IPython terminal

x1 = power_traces_averaged_dB;
y1 = np.array(d_br_collect_co2_ice);
y2 = np.array(d_br_collect_water_ice);
y3 = np.array(d_br_collect_seawater_ice);

class FollowDataWithCursor:

    def __init__(self, ax, x, y):
        self.ax = ax
        #crosshairs
        self.lx = ax.axhline(lw=0.5,color='r')
        self.ly = ax.axvline(lw=0.5,color='r')
        #data variables
        self.x = x
        self.y = y
        #show coordinate values for each plot
        self.txt = ax.text(0.2, 0.01, '', transform=ax.transAxes,fontsize='xx-small')

    def follow_mouse(self, event):
        if not event.inaxes:
            return

        #data values
        x, y = event.xdata, event.ydata
        indx = min(np.searchsorted(self.y, y), len(self.y) - 1)
        x = self.x[indx]
        y = self.y[indx]
        #line locations
        self.lx.set_ydata(y)
        self.ly.set_xdata(x)
        
        self.txt.set_text('x=%1.2f, y=%1.2f' % (x, y))
        self.ax.figure.canvas.draw()

# display visualization
fig, ax = plt.subplots(1,4)

plt.subplot(1,4,1)
plt.vlines(mapping_file[0,2],mapping_file[0,3],mapping_file[0,6],colors='Red')
plt.imshow(rg_3763302,'gray')
plt.xlim([3200,3300])
plt.ylim([1380,1700])
plt.gca().invert_yaxis()
plt.xlabel("pixel # (~460 meters/pixel)")
plt.ylabel("pixel # (0.0375 microseconds/pixel)")

plt.subplot(1,4,2)
l, = plt.plot(x1, y1, lw=1, color='deepskyblue')
l2, = plt.plot(x1,y1,'o',markersize=0.5,color='deepskyblue',label=r'$\epsilon_r$ = 2.1 (CO2 ice)')
plt.gca().invert_yaxis()
plt.title(r'$\epsilon_r$ = 2.1 (CO2 ice)',fontsize='small')
plt.ylabel("depth [meters]")
fig.suptitle("Permittivity-dependent ice thickness in radar sounding")

snap_cursor = FollowDataWithCursor(plt.gca(), x1, y1)
cid = fig.canvas.mpl_connect('motion_notify_event', snap_cursor.follow_mouse)

plt.subplot(1,4,3)
q, = plt.plot(x1, y2, lw=1,color='royalblue')
q2, = plt.plot(x1,y2,'o',markersize=0.5,color='royalblue',label=r'$\epsilon_r$ = 3.15 (water ice)')
plt.gca().invert_yaxis()
plt.title(r'$\epsilon_r$ = 3.15 (water ice)',fontsize='small')
plt.ylabel("depth [meters]")
plt.xlabel("reflection power [dB]")

snap_cursor2 = FollowDataWithCursor(plt.gca(), x1, y2)
cid2 = fig.canvas.mpl_connect('motion_notify_event', snap_cursor2.follow_mouse)

plt.subplot(1,4,4)
w, = plt.plot(x1, y3, lw=1,color='navy')
w2, = plt.plot(x1,y3,'o',markersize=0.5,color='navy',label=r'$\epsilon_r$ = 6.0 (seawater ice)')
plt.gca().invert_yaxis()
plt.title(r'$\epsilon_r$ = 6.0 (seawater ice)',fontsize='small')
plt.ylabel("depth [meters]")

snap_cursor3 = FollowDataWithCursor(plt.gca(), x1, y3)
cid3 = fig.canvas.mpl_connect('motion_notify_event', snap_cursor3.follow_mouse)

fig.set_size_inches(9,5,forward=True)
fig.subplots_adjust(wspace=0.7)

# %%
