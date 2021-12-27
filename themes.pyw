import subprocess
import webbrowser
import os
import sys

from tkinter import *
from tkinter import PhotoImage

root = Tk()
root.title("NuggetOS Themes Selector")
root.geometry('920x680')
root.configure(bg="#1c2e4a")
root.resizable(0,0)

#string values
welcomeText = ("NuggetOS Themes Selector")
subtitleText = ("Select a preinstalled theme from below, or alternatively, open Gnome tweaks to customize even further")

yaruText = ("Yaru - blue accent colour")

lightThemeText = ("☀ Light Theme")
darkThemeText = ("🌙 Dark Theme")

yaruOrangeText = ("Yaru - orange accent colour")

ldThemetext = ("⛅ Light & Dark theme")
viewYaruGithubText = ("View this on GitHub")

gnomeTweaksText = ("Open Gnome Tweaks")

iconsText = ("Icon Themes")
iconsSuruText = ("Suru Icons")
iconsYRDarkText = ("Yaru Dark")
iconsYRLightText = ("Yaru Light")

githubYaruURL = ("https://github.com/Muqtxdir/yaru-remix")
githubYaruOrangeURL = ("https://github.com/ubuntu/yaru")
githubSuruURL = ("https://github.com/snwh/suru-icon-theme/")

#title text
title = Label(root, text=welcomeText)
title.configure(bg="#1c2e4a", fg="#ffffff", font=("Outfit", 25, "bold"))
title.place(x=40, y=20)

#subtitle text
subtitle = Label(root, text=subtitleText)
subtitle.configure(bg="#1c2e4a", fg="#ffffff", font=("Outfit", 14))
subtitle.place(x=40, y=80)

#yaru text
yaruText = Label(root, text=yaruText)
yaruText.configure(bg="#1c2e4a", fg="#ffffff", font=("Outfit", 16, "underline"))
yaruText.place(x=40, y=150)

#change to Yaru Remix Light
def lightTheme():
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "'Yaru-remix-light'"])
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Yaru-remix-light'"])

lightThemeButton = Button(root, text=lightThemeText, fg="white", bg="#5D5AFC", command=lightTheme)
lightThemeButton.configure(font=("Outfit", 16))
lightThemeButton.place(x=40, y=200)

#change to Yaru Remix Dark
def darkTheme():
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "'Yaru-remix-dark'"])
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Yaru-remix-dark'"])

darkThemeButton = Button(root, text=darkThemeText, fg="white", bg="#00008B", command=darkTheme)
darkThemeButton.configure(font=("Outfit", 16))
darkThemeButton.place(x=220, y=200)

#change to both light & dark
def lightDarkTheme():
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "'Yaru-remix'"])
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Yaru-remix'"])

ldThemeButton = Button(root, text=ldThemetext, fg="black", bg="#BCD2E8", command=lightDarkTheme)
ldThemeButton.configure(font=("Outfit", 16))
ldThemeButton.place(x=400, y=200)

#view yaru remix on github
def viewGithubYaru():
	webbrowser.open_new(githubYaruURL)
	
viewYaru = Button(root, text=viewYaruGithubText, fg="white", bg="#474a72", command=viewGithubYaru)
viewYaru.configure(font=("Outfit", 6, 'bold'), width=15, height=1)
viewYaru.place(x=320, y=150)

#yaru orange title
yaruOrangeTitle = Label(root, text=yaruOrangeText)
yaruOrangeTitle.configure(bg="#1c2e4a", fg="#ffffff", font=("Outfit", 16, "underline"))
yaruOrangeTitle.place(x=40, y=300)

#yaru orange normal button
def yaruOrangeLight():
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "'Yaru'"])
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Yaru-remix-light'"])

orangeLightTheme = Button(root, text=lightThemeText, fg="black", bg="#ed7944", command=yaruOrangeLight)
orangeLightTheme.configure(font=("Outfit", 16))
orangeLightTheme.place(x=40, y=350)

#yaru orange dark button
def yaruOrangeDark():
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "'Yaru-dark'"])
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Yaru-remix-light'"])
	
orangeDarkTheme = Button(root, text=darkThemeText, fg="white", bg="#612509", command=yaruOrangeDark)
orangeDarkTheme.configure(font=("Outfit", 16))
orangeDarkTheme.place(x=220, y=350)

#view orange on github
def viewGithubYaruOrange():
	webbrowser.open_new(githubYaruOrangeURL)
	
viewYaruOrange = Button(root, text=viewYaruGithubText, fg="white", bg="#474a72", command=viewGithubYaruOrange)
viewYaruOrange.configure(font=("Outfit", 6, 'bold'), width=15, height=1)
viewYaruOrange.place(x=320, y=300)

#icon theme title
yaruText = Label(root, text=iconsText)
yaruText.configure(bg="#1c2e4a", fg="#ffffff", font=("Outfit", 16, "underline"))
yaruText.place(x=40, y=450)

#suru icons
def suruIconTheme():
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Suru'"])

suruIconsButton = Button(root, text=iconsSuruText, fg="black", bg="#ed7944", command=suruIconTheme)
suruIconsButton.configure(font=("Outfit", 16))
suruIconsButton.place(x=40, y=500)

#yaru remix light icons (iconsYRLightText)
def yaruLightIcons():
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Yaru-remix-light'"])
	
yaruLightIconsButton = Button(root, text=iconsYRLightText, fg="white", bg="#5D5AFC", command=yaruLightIcons)
yaruLightIconsButton.configure(font=("Outfit", 16))
yaruLightIconsButton.place(x=220, y=500)

#yaru remix dark icons
def yaruDarkIcons():
	subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "'Yaru-remix-dark'"])

yaruDarkIconsButton = Button(root, text=iconsYRDarkText, fg="white", bg="#00008b", command=yaruDarkIcons)
yaruDarkIconsButton.configure(font=("Outfit", 16))
yaruDarkIconsButton.place(x=400, y=500)

#view suru remix on github
def viewGithubSuru():
	webbrowser.open_new(githubSuruURL)
	
viewSuru = Button(root, text=viewYaruGithubText, fg="white", bg="#474a72", command=viewGithubSuru)
viewSuru.configure(font=("Outfit", 6, 'bold'), width=15, height=1)
viewSuru.place(x=320, y=450)

#gnome-tweaks - a button that calls that program for further personalization
def gnomeTweaks():
	os.system("gnome-tweaks")

openGnomeTweaks = Button(root, text=gnomeTweaksText, fg="white", bg="#474a72", command=gnomeTweaks)
openGnomeTweaks.configure(font=("Outfit", 12, "italic"))
openGnomeTweaks.place(x=40, y=600)

root.mainloop()
