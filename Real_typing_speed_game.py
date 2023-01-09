import random
from tkinter import *
from tkinter import messagebox
from PIL import Image
import time



def animination(count_images):
    global anim
    new_image_variable = images[count_images]
    mainframe_frame_label.configure(image=new_image_variable)
    count_images = count_images + 1

    if count_images == no_of_frames:
        count_images = 0

    anim = root.after(30,lambda: animination(count_images))

def countdown_for_starting_game():
    global countdown
    if countdown>1:
        countdown=countdown-1
        countdown1_label.place(x=1, y=1)
        countdown1_label.configure(text=countdown)
        countdown2_label.place(x=1, y=1)
        countdown2_label.configure(text=countdown)
        stop_time.after(1000,countdown_for_starting_game)
    elif countdown==1:
        countdown1_label.configure(text='Go')
        countdown2_label.configure(text='Go')
        countdown = countdown - 1
        stop_time.after(1000,countdown_for_starting_game)
    else:
        changelevel_label.place_forget()
        word_given.grid(row=2, column=2, padx=1, pady=1)
        countdown1_label.place_forget()
        countdown2_label.place_forget()
        start_time.configure(text=time_remaning)
        word_given.configure(text=words_list[0])
        timer_started()

def play_again():
    global countdown,count,word_slider,count_score,count_missed_score,time_remaning,changetime

    messagebox.showinfo("Warning ", "*********** Do You Want To Continue ************")
    occuracy_label.place_forget()
    score_label.place_forget()
    count=0
    word_slider=''
    count_score=0
    count_missed_score=0
    time_remaning=changetime
    countdown=4
    correct.configure(text=count_score)
    incorrect.configure(text=count_missed_score)
    start_time.configure(text=' ')
    stop_time.configure(text=' ')
    countdown1_label.place(x=100, y=550)
    countdown2_label.place(x=640, y=550)
    animination(count_images)
    countdown_for_starting_game()


def slider1():
    global count,word_slider
    text='TYPING SPEED GAME'
    if(count>=len(text)):
        count=0
        word_slider=''
    word_slider+=text[count]
    count+=1
    name_of_game1.configure(text=word_slider)
    name_of_game1.after(350,slider1)

def slider2():
    global count,word_slider
    text='TYPING SPEED GAME'
    if(count>=len(text)):
        count=0
        word_slider=''
    word_slider+=text[count]
    count+=1
    name_of_game2.configure(text=word_slider)
    name_of_game2.after(350,slider2)


#######################  saving and clearing  the entry content  ########################

def saving_and_clearing_entry_content(event):
    global count_score,count_missed_score

    if word_write.get()==word_given['text']:
        count_score=count_score+1
        correct.configure(text=count_score)
    else:
        count_missed_score=count_missed_score+1
        incorrect.configure(text=count_missed_score)

    random.shuffle(words_list)
    word_given.configure(text=words_list[0])
    word_write.delete(0,END)


def timer_started():
    global time_remaning

    if time_remaning > 0:
        time_remaning = time_remaning - 1
        start_time.configure(text='0')
        stop_time.configure(text=time_remaning)
        stop_time.after(1000, timer_started)
    else:

        root.after_cancel(anim)
        word_given.grid_remove()
        changelevel_label.place(x=90, y=25)
        messagebox.showinfo("Warning ", "*************** Game End ****************")
        your_score.configure(text=count_score)
        total_count=count_score+count_missed_score
        try:
            occuracy_count=(count_score/total_count)*100
            actual_occuracy_count=str("{:.2f}".format(occuracy_count))
            actual_occuracy_count=actual_occuracy_count+"%"
            occuracy.configure(text=actual_occuracy_count)
            score_label.place(x=7, y=525)
            occuracy_label.place(x=660, y=525)
        except:
            occuracy_count=0
            actual_occuracy_count=str("{:.2f}".format(occuracy_count))
            actual_occuracy_count=actual_occuracy_count+"%"
            occuracy.configure(text=actual_occuracy_count)
            score_label.place(x=7, y=525)
            occuracy_label.place(x=660, y=525)



def Choose_level():
    global anim_for_loading
    mainlabel.grid_remove()
    root.after_cancel(anim_for_loading)
    create()

def lets_go():

    global start_button,countdown1_label,countdown2_label,name_of_game1,name_of_game2,count,word_slider,mainframe_frame
    global word,word_write,word_given,words_list,count_score,count_missed_score,correct,incorrect,time_remaning
    global stop_time,countdown,start_time,score_label,occuracy_label,your_score,occuracy,Gif,images,anim
    global mainframe_frame_label,no_of_frames,count_images,changelevel_label,level,mainlabel


    front_page.grid_remove()

    start_button = PhotoImage(file='game_start_button.png')
    level = PhotoImage(file="levelup.png")

    start_button = start_button.subsample(9, 9)
    level = level.subsample(9, 9)

    #################### putting gif #################

    information = Image.open('gif2.gif')
    no_of_frames = information.n_frames
    print(no_of_frames)
    images = []
    for i in range(no_of_frames):
        Gif=PhotoImage(file='gif2.gif', format=f'gif -index {i}')
        Gif=Gif.subsample(5,5)
        images.append(Gif)

    count_images=0

    anim = None

    count=0
    word_slider=''
    count_score=0
    count_missed_score=0
    time_remaning=changetime
    countdown=4

    mainlabel=LabelFrame(root,bg='gray17',width=880,height=1500,borderwidth=0)
    mainlabel.grid(row=0,column=0,padx=2,pady=5,rowspan=3)

    name_of_game1_frm=LabelFrame(mainlabel,bg='gray',width=50,height=370,borderwidth=0)
    name_of_game1_frm.grid(row=0,column=0,padx=3,pady=3,rowspan=3)

    name_of_game1_label=Label(name_of_game1_frm,bg='cyan2',width=10,height=25)
    name_of_game1_label.grid(row=0,column=0,padx=1,pady=1,rowspan=3)

    name_of_game1_frame=LabelFrame(name_of_game1_label,bg='gray30',width=70,height=370,bd=10)
    name_of_game1_frame.grid(row=0,column=0,padx=1,pady=1,rowspan=3)

    name_of_game1=Label(name_of_game1_frame,bg='gray17',text=" ",font=('arial',19,'italic bold'),width=3,height=16,
                        wraplength=1,fg='aquamarine')
    name_of_game1.grid(row=0,column=0,padx=1,pady=1,rowspan=2)

    mainframe_frm= LabelFrame(mainlabel, bg='gray17', width=550, height=270,borderwidth=0)
    mainframe_frm.grid(row=0, column=1, padx=1, pady=1,columnspan=3)

    mainframe_label=Label(mainframe_frm,bg='cyan2',width=70,height=20)
    mainframe_label.grid(row=0,column=1,padx=5,pady=1,columnspan=3)

    mainframe_frame= LabelFrame(mainframe_label, bg='gray30', width=550, height=270,bd=10,text='Pankaj Singh Raikwal',
                                 font=('arial',14,'italic bold'),fg='aquamarine')
    mainframe_frame.grid(row=0, column=1, padx=1, pady=1,columnspan=3)

    mainframe_frame_label=Label(mainframe_frame,bg='gray17')
    mainframe_frame_label.grid(row=0, column=0, padx=1, pady=1, columnspan=3)

    animination(count_images)

    name_of_game2_frm=LabelFrame(mainlabel,bg='gray17',width=50,height=370,borderwidth=0)
    name_of_game2_frm.grid(row=0,column=4,padx=3,pady=3,rowspan=3)

    name_of_game2_label=Label(name_of_game2_frm,bg='cyan2',width=10,height=25)
    name_of_game2_label.grid(row=0,column=4,padx=1,pady=1,rowspan=3)

    name_of_game2_frame=LabelFrame(name_of_game2_label,bg='gray30',width=70,height=370,bd=10)
    name_of_game2_frame.grid(row=0,column=4,padx=1,pady=1,rowspan=3)

    name_of_game2=Label(name_of_game2_frame,bg='gray17',text=" ",font=('arial',19,'italic bold'),width=3,height=16,
                        wraplength=1,fg='aquamarine')
    name_of_game2.grid(row=0,column=0,padx=1,pady=1,rowspan=2)

    slider1()
    slider2()

    start_time_frm=LabelFrame(mainlabel,bg='gray30',width=180,height=80,borderwidth=0)
    start_time_frm.grid(row=1,column=1,padx=5,pady=5)

    start_time_label=Label(start_time_frm,bg='cyan2',width=15,height=5)
    start_time_label.grid(row=1,column=1,padx=1,pady=1)

    start_time_frame=LabelFrame(start_time_label,bg='gray30',width=180,height=80,bd=10,text='Starting Time ',
                                font=('arial',14,'italic bold'),fg='aquamarine')
    start_time_frame.grid(row=1,column=1,padx=1,pady=1)

    start_time=Label(start_time_frame,bg='gray17',width=12,height=2,text=' ',font=('arial',16,'italic bold '),bd=5,
                     fg='aquamarine')
    start_time.grid(row=0,column=0,padx=1,pady=1)

    startbutton_frame =LabelFrame(mainlabel,bg='gray17',width=12,height=2,borderwidth=0)
    startbutton_frame.grid(row=1,column=2,padx=5,pady=5)

    startbutton_label=Label(startbutton_frame, bg='gray17', width=100, height=50)
    startbutton_label.grid(row=1,column=2,padx=5,pady=5)

    start_buttons=Button(startbutton_label,image=start_button,width=53,bd=5,borderwidth=0,bg='gray17',
                         command=countdown_for_starting_game,activebackground="gray17",fg='aquamarine')
    start_buttons.grid(row=1,column=2,padx=5,pady=5)

    stop_time_frm=LabelFrame(mainlabel,bg='gray',width=180,height=80,borderwidth=0)
    stop_time_frm.grid(row=1,column=3,padx=5,pady=5)

    stop_time_label=Label(stop_time_frm,bg='cyan2',width=15,height=5)
    stop_time_label.grid(row=1,column=3,padx=1,pady=1)

    stop_time_frame=LabelFrame(stop_time_label,bg='gray30',width=180,height=80,bd=10,text='Remaning Time ',
                                font=('arial',14,'italic bold'),fg='aquamarine')
    stop_time_frame.grid(row=1,column=3,padx=1,pady=1)

    stop_time=Label(stop_time_frame,bg='gray17',width=13,height=2,text=' ',font=('arial',15,'italic bold '),bd=5,
                     fg='aquamarine')
    stop_time.grid(row=0,column=0,padx=1,pady=1)

    changing_word_with_level= LabelFrame(mainlabel, bg='gray17', width=253, height=114,borderwidth=0)
    changing_word_with_level.grid(row=2,column=2,padx=1,pady=1)

    word_given=Label(changing_word_with_level,bg='gray17',width=15,height=3,bd=10,text=' ' ,font=('arial',18,'bold '),
                     fg='aquamarine')
    word_given.place(x=2,y=2)
    word_given.grid_remove()

    ################ Taking the words from user frame creating ################

    word=StringVar()
    word_write=Entry(mainlabel,bg='gray15',width=20,bd=8,text=word,font=('arial',18,'bold '),fg='aquamarine',justify=CENTER)
    word_write.grid(row=3,column=2,padx=5,pady=5)
    word_write.focus_set()

    ####################### for saving and clearing  the entry content binding the enter button  ########################
    root.bind('<Return>',saving_and_clearing_entry_content)

    ################### incorrect #########################

    incorrect_frm=LabelFrame(mainlabel,bg='gray17',width=193,height=117,borderwidth=0)
    incorrect_frm.place(x=95,y=400)

    incorrect_label=Label(incorrect_frm,bg='cyan2',width=26,height=7)
    incorrect_label.place(x=1,y=1)

    incorrect_frame=LabelFrame(incorrect_label,bg='gray30',width=181,height=89,bd=10,text='Incorrect',
                                font=('arial',14,'italic bold'),fg='aquamarine')
    incorrect_frame.place(x=1,y=1)

    incorrect=Label(incorrect_frame,bg='cyan2',width=10,height=2,text='0',font=('arial',18,'italic bold '),bd=5,
                     fg='dark blue')
    incorrect.grid(row=0,column=0,padx=0,pady=0)

    ########################  change  level ##########################

    changelevel_label = Label(changing_word_with_level, bg='gray17', width=100, height=50)
    changelevel_label.place(x=90, y=25)

    choose_level_button=Button(changelevel_label,image=level,bg="gray17",bd=0,activebackground="gray17",command=Choose_level)
    choose_level_button.grid(row=0,column=0,padx=5,pady=2)

    ###############  correct #########################

    correct_frm=LabelFrame(mainlabel,bg='gray17',width=193,height=117,borderwidth=0)
    correct_frm.place(x=591,y=400)

    correct_label=Label(correct_frm,bg='cyan2',width=26,height=7)
    correct_label.place(x=1,y=1)

    correct_frame=LabelFrame(correct_label,bg='gray30',width=181,height=89,bd=10,text='Correct',
                                font=('arial',14,'italic bold'),fg='aquamarine')
    correct_frame.place(x=1,y=1)

    correct=Label(correct_frame,bg='cyan2',width=10,height=2,text='0',font=('arial',18,'italic bold '),bd=5,
                     fg='dark blue')
    correct.grid(row=0,column=0,padx=0,pady=1)

    ##################### countdown creation ####################

    countdown1_frame=LabelFrame(mainlabel,bg='gray17', width=135, height=60,borderwidth=0)
    countdown1_frame.place(x=100,y=550)

    countdown1_label=Label(countdown1_frame,bg='gray17',width=5,height=1,text=countdown,
                           font=('arial',30,'italic bold'),fg='aquamarine')
    countdown1_label.place(x=1,y=1)
    countdown1_label.place_forget()

    countdown2_frame=LabelFrame(mainlabel,bg='gray17', width=135, height=60,borderwidth=0)
    countdown2_frame.place(x=640,y=550)

    countdown2_label=Label(countdown2_frame,bg='gray17',width=5,height=1,text=countdown,font=('arial',30,'italic bold'),fg='aquamarine')
    countdown2_label.place(x=1,y=1)
    countdown2_label.place_forget()


    #################play agin button ctreation ############

    play_again_label=Label(mainlabel,bg='cyan2',width=15,height=5)
    play_again_label.grid(row=4,column=2,padx=5,pady=10)

    play_again_frame=Button(play_again_label,bg='gray17',width=10,height=1,bd=4,text='Play Again ',activeforeground='violet',
                                font=('arial',14,'italic bold'),fg='aquamarine',activebackground='gray17',command=play_again)
    play_again_frame.grid(row=4,column=2,padx=1,pady=1)

    #################### your score frame creating ############################

    score_label=Label(mainlabel,bg='cyan2',width=26,height=7)
    score_label.place(x=7,y=525)

    score_frame=LabelFrame(score_label,bg='gray30',width=181,height=89,bd=10,text='Score ',
                                font=('arial',14,'italic bold'),fg='aquamarine')
    score_frame.place(x=1,y=1)

    your_score=Label(score_frame,bg='cyan2',width=10,height=2,text=' ',font=('arial',18,'italic bold '),bd=5,
                     fg='dark blue')
    your_score.grid(row=0,column=0,padx=0,pady=1)

    score_label.place_forget()

    ################## your accuracy frame creating #######################

    occuracy_label=Label(mainlabel,bg='cyan2',width=26,height=7)
    occuracy_label.place(x=660,y=525)

    occuracy_frame=LabelFrame(occuracy_label,bg='gray30',width=181,height=89,bd=10,text='Ocurracy',
                                font=('arial',14,'italic bold'),fg='aquamarine')
    occuracy_frame.place(x=1,y=1)

    occuracy=Label(occuracy_frame,bg='cyan2',width=10,height=2,text=' ',font=('arial',18,'italic bold '),bd=5,
                     fg='dark blue')
    occuracy.grid(row=0,column=0,padx=0,pady=1)
    occuracy_label.place_forget()




def Nobutton():
    global counter
    print("value of count:- ",counter)
    for x in range(2, 293):
        contouine_label.place(x=-x, y=2)
        loading_label.update()
    for k in range(1,330):
        yes_no_button_label.place(x=-k, y=2)
        yes_no_button_frame.update()
    counter=1
    label_for_confirmation.config(text=' ')
    messagebox.showinfo("Choose","Please Choose The Difficulty Level.\n\n Thank You")

#################### function for easy button property ################
global easy_count
easy_count=False
global check1
check1=1

global Medium_count
Medium_count=False
global check2
check2=1

global Hard_count
Hard_count=False
global check3
check3=1

global yesbutton_check
yesbutton_check=True

def easy_button_property():
    global counter,changetime,words_list,easy_count,check1,check2,check3,yesbutton_check
    changetime=151

    words_list=['cougar','able','about','above','accept','heart','account','across','act','action','tweet','friend'
        ,'add','address','meme','admit','adult','affect','after','again','against','age','agency','agent','ago',
        'agree',' viral','ahead','air','all','allow','almost','alone','along','already','also','although','always',
        'rock','among','amount','pimp','animal','another','answer','anyone','anything','appear','apply','approach',
        'area','argue','arm','around','arrive','art','article','artist','assume','attack','attention','attorney','audience'
        ,'author','own','available']

    label_for_confirmation.config(text='You Have chosen Easy')
    print("value of count:- ",counter)
    check1=check1+1
    print("value of check1 :- ",check1)
    yesbutton_check=True
    if check1>2:
        easy_count=True

    if(counter==1):
        for x in range(-293,2):
            contouine_label.place(x=x,y=2)
            loading_label.update()
        for x in range(-330,1):
            yes_no_button_label.place(x=x,y=2)
            yes_no_button_frame.update()
        counter=counter+1
    elif easy_count==True:
        easy_count=False
        messagebox.showinfo("Warning"," You have already choosen this option !! \n \n Thank You.")
    else:
        check1=1
        check2=1
        check3=1
        label_for_confirmation.config(text='')
        yesbutton_check=False
        messagebox.showinfo("Warning"," Click on No button for choosing the other option!!")


#################### function for easy button property ################
def Medium_button_property():
    global counter,changetime,words_list,check1,Medium_count,check3,check2,yesbutton_check
    changetime=101
    words_list=['comply','able','about','above','accept','concept','account','across','act','action','activity','context'
        ,'add','efficient','classic','admit','adult','affect','after','again','against','age','agency','agent','ago',
        'agree','covert','ahead','air','all','allow','almost','alone','along','already','also','although','always',
        'abash','among','amount','abate','animal','another','answer','anyone','effective','appear','apply','approach',
        'area','argue','arm','around','arrive','art','article','artist','assume','attack','bias','elliptical','audience'
        ,'author','canny','chaff']

    label_for_confirmation.config(text='You Have chosen Medium')
    print("value of count:- ",counter)

    check2 = check2 + 1
    print("value of check2 :- ",check2)
    yesbutton_check = True
    if check2>2:
        Medium_count=True

    if(counter==1):
        for x in range(-293,2):
            contouine_label.place(x=x,y=2)
            loading_label.update()
        for x in range(-330,1):
            yes_no_button_label.place(x=x,y=2)
            yes_no_button_frame.update()
        counter=counter+1

    elif Medium_count == True:
        Medium_count = False

        messagebox.showinfo("Warning", " You have already choosen this option !! \n \n Thank You.")

    else:
        check2 = 1
        check1 = 1
        check3=1
        label_for_confirmation.config(text='' )
        yesbutton_check = False
        messagebox.showinfo("Warning", " Click on No button for choosing the other option!!")

#################### function for easy button property ################
def Hard_button_property():
    global counter,changetime,words_list,check3,Hard_count,check2,check1,yesbutton_check
    changetime=51

    words_list=['adumbrate','Worcestershire','about','abnegation','accept','according','account','across','act','action','activity','actually'
        ,'aggrandize','address','administration','admit','Personalized','corpulence','Unfortunately','again','against','starvation','agency','agent','Morocco',
        'compunction','agreement','ahead','antediluvian','anathema','blandishment','almost','camaraderie','circumvent','already','also','although','always',
        'American','ambivalent','amount','analysis','animal','another','answer','anyone','anything','appear','Onomatopoeia','approach',
        'contentious','contentious','Sesquipedalian','around','arrive','Phenomenon','article','artist','assume','attack','attention','attorney','audience'
        ,'author','authority','available']

    label_for_confirmation.config(text='You Have chosen Hard')
    print("value of count:- ",counter)

    check3 = check3 + 1
    print("value of check2 :- ",check3)
    yesbutton_check = True
    if check3>2:
        Hard_count=True

    if(counter==1):
        for x in range(-293,2):
            contouine_label.place(x=x,y=2)
            loading_label.update()
        for x in range(-330,1):
            yes_no_button_label.place(x=x,y=2)
            yes_no_button_frame.update()
        counter=counter+1
    elif Hard_count == True:
        Hard_count = False
        messagebox.showinfo("Warning", " You have already choosen this option !! \n \n Thank You.")

    else:
        check2 = 1
        check1 = 1
        check3=1
        label_for_confirmation.config(text='')
        yesbutton_check = False
        messagebox.showinfo("Warning", " Click on No button for choosing the other option!!")


def animination1(count_images_for_loading):
    global anim_for_loading,calc
    load_gif=Label(loading_gif_label,width=400,height=200,bg="black")
    load_gif.place(x=18, y=5)
    new_image_variable1 = images_for_loading[count_images_for_loading]
    load_gif.configure(image=new_image_variable1)
    count_images_for_loading = count_images_for_loading + 1
    if count_images_for_loading == no_of_frames_loading:
        count_images_for_loading = 0
    calc=calc+1
    if(calc==80):
        print(calc)
        lets_go()
    anim_for_loading = root.after(50,lambda: animination1(count_images_for_loading))

def donothing():
    return "You have not choosen difficulty level \n Click NO button for selecting difficulty level !!"

def show():
    global yesbutton_check
    if(yesbutton_check==True):
        wating_label.place(x=5, y=3)
        animination1(count_images_for_loading)
    else:
        text=donothing()
        messagebox.showinfo("Warning", text)

def create():
    global my_image,corrected,images_for_loading,loading_gif_label,no_of_frames_loading,count_images_for_loading
    global anim_for_loading,label_for_confirmation,easy_image,medium_image,hard_image,not_corrected,contouine_label
    global loading_label,yes_button,no_button,yes_no_button_label,yes_no_button_frame,front_page,wating_label


    global front_page_label,count

    global counter
    counter = 1
    global calc
    calc = 1

    ########## inserting the image in our project ###########
    my_image=PhotoImage(file="pankaj.png")
    easy_image=PhotoImage(file="easy.png")
    medium_image=PhotoImage(file="medium.png")
    hard_image=PhotoImage(file="hard.png")
    corrected=PhotoImage(file="yes.png")
    not_corrected = PhotoImage(file="click.png")


    ########## resizing the images ############
    my_image = my_image.subsample(1, 1)
    easy_image=easy_image.subsample(15,15)
    medium_image=medium_image.subsample(15,15)
    hard_image=hard_image.subsample(15,15)
    corrected = corrected.subsample(7, 7)
    not_corrected=not_corrected.subsample(7, 7)

    ################ creating the label for front page ################
    front_page = LabelFrame(root, bg='black', width=125, height=45,borderwidth=0)
    front_page.grid(row=0, column=0, padx=0, pady=0)

    front_page_label = Label(front_page, bg='black', width=125, height=45)
    front_page_label.grid(row=0, column=0, padx=0, pady=0)

    front_frame=LabelFrame(front_page_label,bg='black',width=868,height=660,borderwidth=0)
    front_frame.place(x=1,y=1)

    ################## creaing the frames  and label for my image and putting my image also  #############

    image_label_frame=LabelFrame(front_frame,bg="gray10",width=350,height=350,text="Created By ",bd=8,
                                 font=("arial",14,'italic bold'),fg="aquamarine")
    image_label_frame.place(x=30,y=10)

    image_border_label=Label(image_label_frame,bg='cyan2',width=55,height=23)
    image_border_label.grid(row=0,column=0,padx=5,pady=5)

    image_putting_frame=LabelFrame(image_border_label,bg="gray10",width=380,height=300,text="Pankaj Singh Raikwal ",
                                 font=("arial",14,'italic bold'),fg="aquamarine")
    image_putting_frame.grid(row=0,column=0,padx=2,pady=2)

    image_label=Label(image_putting_frame,bg='gray10',width=190,height=175,image=my_image)
    image_label.grid(row=0,column=0,padx=9,pady=4)

    ################ label for selecting the dificulty level ###################

    label_for_dificulties = Label(front_page_label, width=29, height=2, text="Please Choose The Difficulty Level ",
                                  font=('arial', 25, "italic bold"), fg='aquamarine', bg='black')
    label_for_dificulties.place(x=290, y=20)

    ################## creating button for difficulty level ################

    easy_button = Button(front_page_label, width=170, height=39, text="Easy ", font=("new roman", 28, "bold "),
                         bg='gray17',
                         fg='cyan2', activebackground="gray17", activeforeground="cyan2", bd=5, image=easy_image,
                         compound=RIGHT,
                         command=easy_button_property)
    easy_button.place(x=480, y=110)

    medium_button = Button(front_page_label, width=205, height=39, text="Medium  ", font=("new roman", 28, "bold"),
                           bg='gray17',
                           fg='cyan2', activebackground="gray17", activeforeground="cyan2", bd=5, image=medium_image,
                           compound=RIGHT,
                           command=Medium_button_property)
    medium_button.place(x=462, y=180)

    hard_button = Button(front_page_label, width=170, height=39, text="Hard  ", font=("new roman", 28, "bold"),
                         bg='gray17',
                         fg='cyan2', activebackground="gray17", activeforeground="cyan2", bd=5, image=hard_image,
                         compound=RIGHT,
                         command=Hard_button_property)
    hard_button.place(x=480, y=250)

    ########################### label for confirmation ##################
    label_for_confirmation = Label(front_page_label, width=22, height=1, bg='gray17', text="",
                                   font=("arial", 18, 'italic bold '), fg="cyan2")
    label_for_confirmation.place(x=405, y=330)

    ################### label for loading the gif ##################
    loading_label=LabelFrame(front_page_label, width=405, height=200, bg='black',borderwidth=0)
    loading_label.place(x=400, y=430)

    loading_gif_label = Label(loading_label, width=150, height=130, bg='black')
    loading_gif_label.place(x=5, y=5)

    load_gif=Label(loading_gif_label,width=45,height=10,bg="black")
    load_gif.place(x=18, y=5)

    load_gif.place_forget()

    ################ including gif in our project ####################
    information_for_loading = Image.open('load.gif')
    no_of_frames_loading = information_for_loading.n_frames
    print(no_of_frames_loading)
    images_for_loading = []
    for i in range(no_of_frames_loading):
        loading_gif = PhotoImage(file='load.gif', format=f'gif -index {i}')
        loading_gif = loading_gif.subsample(3,3)
        images_for_loading.append(loading_gif)

    count_images_for_loading = 0

    anim_for_loading = None

    ################## label for contiouning the game  ################

    countinue = LabelFrame(front_page_label, width=300, height=85, bg='black',borderwidth=0)
    countinue.place(x=0, y=320)

    contouine_label = Label(countinue, width=15, height=2, bg='black', text=" Do You Want \n To Continue ?",
                            font=("arial", 23, "italic bold "), fg='aquamarine')
    contouine_label.place(x=-293,y=2)


    ####################  yes no button ####################

    yes_no_button_frame=LabelFrame(front_frame,width=330,height=80,bg='black',borderwidth=0)
    yes_no_button_frame.place(x=0,y=410)

    yes_no_button_label = LabelFrame(yes_no_button_frame, width=330, height=80, bg='black', borderwidth=0)
    yes_no_button_label.place(x=-330, y=2)

    yes_button = Button(yes_no_button_label, width=78, height=73, bg='black', activebackground="black",
                        bd=0, image=corrected, command=show)
    yes_button.place(x=12, y=2)

    no_button = Button(yes_no_button_label, width=78, height=73, bg='black', activebackground="black",
                       bd=0, image=not_corrected,command=Nobutton)
    no_button.place(x=223, y=2)

    yes_no_button_label.place_forget()

    wating_frame=LabelFrame(front_page_label,width=520,height=110,bg='black',borderwidth=0)
    wating_frame.place(x=1,y=500)

    wating_label = Label(wating_frame, width=30, height=2, bg='black', text=" PLease Wait your Page Is Loading...",
                         font=("Segoe Print", 20, "italic bold "), fg='aquamarine')
    wating_label.place(x=5, y=3)
    wating_label.place_forget()

root=Tk()
root.geometry("880x630+200+0")
root.configure(bg="gray17")
root.resizable(False,False)
root.iconbitmap('keybord.ico')
root.title('TYPING SPEED TEXT GAME ')
create()
root.mainloop()