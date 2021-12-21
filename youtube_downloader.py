import PIL.Image
from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube

folder_name = ''

def makeCenter(root):
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth()//2) - (width//2)
	y = (root.winfo_screenheight()//2) - (height//2)
	root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def openLocation():
	global folder_name
	folder_name = filedialog.askdirectory()
	if len(folder_name)>0:
		folder_location.config(text=folder_name, foreground='green')
	else:
		folder_location.config(text='Chọn thư mục', foreground='red')

def DownloadVideo():
	link = link_entry.get()
	choice = quality_choice.get()
	if len(link)>0 and len(choice)>0 and len(folder_name)>0:
		try:
			yt = YouTube(link)
			flag = True
		except:
			flag = False
			messagebox.showerror(title='Lỗi', message='Không thể tải, vui lòng kiểm tra lại link !!!')
		if flag:
			if choice == qualities[0]:
				select = yt.streams.get_highest_resolution()
				select.download(folder_name)
				messagebox.showinfo(title='Thông báo', message='Tải video thành công !!!')
			elif choice == qualities[1]:
				select = yt.streams.filter(only_audio=True).first()
				select.download(folder_name)
				messagebox.showinfo(title='Thông báo', message='Tải audio thành công !!!')
			else:
				messagebox.showerror(title='Lỗi', message='Vui lòng chọn lại loại cần tải !!!')
	else:
		if len(link)==0:
			messagebox.showerror(title='Lỗi', message='Vui lòng nhập link !!!')
		elif len(choice)==0:
			messagebox.showerror(title='Lỗi', message='Vui lòng chọn loại cần tải !!!')
		else:
			messagebox.showerror(title='Lỗi', message='Vui lòng chọn thư mục để lưu !!!')

root = Tk()
root.title('Youtube Downloader')
root.geometry("600x250")
makeCenter(root)
root.iconbitmap("youtube.ico")
root.resizable(width = False, height = False)

load = PIL.Image.open("background_night.jpg")
render = ImageTk.PhotoImage(load)
img=Label(root, image = render)
img.place(x=-200,y=-100)

label = Label(root, text = 'DOWNLOAD FROM YOUTUBE', font=('digital-7', 20), foreground='white', background="#03152D").pack(pady=10)

frame_link = Frame(root)
link_var = StringVar()
link_label = Label(frame_link, text='   Nhập link:', width=15)
link_label.pack(side=LEFT)
link_entry = Entry(frame_link, width=50, textvariable=link_var)
link_entry.pack()
frame_link.pack(pady=10)

quality_frame = Frame(root)
qualities = ["Video", "Audio"]
quality_label = Label(quality_frame, text='   Chọn loại: ', width=15)
quality_label.pack(side=LEFT)
quality_choice = Combobox(quality_frame, values=qualities, width=47)
quality_choice.pack()
quality_frame.pack(pady=5)

frame_folder = Frame(root)
folder_button = Button(frame_folder, width=15, text='Chọn thư mục', command=openLocation)
folder_button.pack(side=LEFT)
folder_location = Label(frame_folder,width=50)
folder_location.pack()
frame_folder.pack(pady=5)

download_button = Button(root, text='Tải', width=10, command=DownloadVideo)
download_button.pack(pady=25)

root.mainloop()