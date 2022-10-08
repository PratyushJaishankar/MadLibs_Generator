from tkinter import *
base = Tk()
base.title("Mad Libs Generator")
base.geometry('360x300')
base.background='#edeae1'
base.resizable(False, False)
Label(base, font=("Nunito", 17), text='Mad Libs Generator').place(x=80, y=0)
Label(base, font=("Nunito", 17), text='Enjoy!').place(x=140, y=35)
ml1 = Button(base, text='The Gold', font=("Nunito", 17), command=lambda: first_madlib(base), bg='#87cefa')
ml1.place(x=125, y=90)
ml2 = Button(base, text='One Dark, Stormy Night', font=("Nunito", 17), command=lambda: second_madlib(base) , bg='#87cefa')
ml2.place(x=50, y=150)
ml3 = Button(base, text='The Ring', font=("Nunito", 17), command=lambda: third_madlib(base), bg='#87cefa')
ml3.place(x=125, y=210)
def first_madlib(win):
  def final_madlib(zh: Toplevel, beast, guardian, month, pathway, motion, n):
    text = f'''
There was once a {beast}. He was always reprimanded. One day while his {guardian} was sitting in the garden in {month}, he sneaked out. He did not mean to go far but he saw a sparkling thing on the {pathway} and {motion} over to it. He observed it to be gold and became wealthy because he had {n} portions of gold🤩🤩.So luckyyy!!!.'''
    zh.geometry(newGeometry='380x560')
    Label(zh, text='Your Story:', font=("Raleway", 13, 'bold'), background='#FFD700', wraplength=zh.winfo_width()).place(x=130, y=310)
    Label(zh, text=text, font=("Raleway", 13), background='#FFD700', wraplength=zh.winfo_width()).place(x=0, y=330)
  frame1 = Toplevel(win, bg='#FFD700')
  frame1.title("The Gold")
  frame1.geometry('380x560')
  frame1.resizable(False, False)
  Label(frame1, text='The Gold - Mad Libs', font=("Raleway", 20, 'bold'), bg='#FFD700').place(x=60, y=0)
  Label(frame1, text='An beast:', font=("Raleway", 16), bg='#FFD700').place(x=0, y=35)
  Label(frame1, text='Choose a guardian:', font=("Raleway", 16), bg='#FFD700').place(x=0, y=70)
  Label(frame1, text='Choose a month:', font=("Raleway", 16), bg='#FFD700').place(x=0, y=110)
  Label(frame1, text='Choose a pathway:', font=("Raleway", 16), bg='#FFD700').place(x=0, y=150)
  Label(frame1, text='Choose a movement type:', font=("Raleway", 16), bg='#FFD700').place(x=0, y=190)
  Label(frame1, text='A number:', font=("Raleway", 16), bg='#FFD700').place(x=0, y=230)
  animal_entry = Entry(frame1, width=17)
  animal_entry.place(x=250, y=35)
  n_entry = Entry(frame1, width=17)
  n_entry.place(x=250, y=230)
  guardians = ['Mum', "Dad"]
  months = ['Jan', 'Feb', 'March', 'April', 'May', 'June',
            'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
  motion = ['walked', 'ran']
  paths = ['cemented', 'dusty']
  guardian_opt = StringVar(frame1)
  guardian_opt.set(guardians[0])
  OptionMenu(frame1, guardian_opt, *guardians).place(x=270, y=70)
  month_opt = StringVar(frame1)
  month_opt.set(months[0])
  OptionMenu(frame1, month_opt, *months).place(x=255, y=110)
  path_opt = StringVar(frame1)
  path_opt.set(paths[0])
  OptionMenu(frame1, path_opt, *paths).place(x=270, y=150)
  motion_opt = StringVar(frame1)
  motion_opt.set(motion[0])
  OptionMenu(frame1, motion_opt, *motion).place(x=265, y=190)
  enter_button = Button(frame1, text="Submit", background="SteelBlue", font=('Raleway', 12), command=lambda:final_madlib(frame1, animal_entry.get(), guardian_opt.get(), month_opt.get(), path_opt.get(), motion_opt.get(), n_entry.get()))
  enter_button.place(x=150, y=270)
  frame1.mainloop()
def second_madlib(win):
  def final_madlib(zh: Toplevel, child, cloth, organism, adjective, village, exclamation, favourite):
    text = f'''
On a dark night, stormy, {child} arrived. He was wearing nothing other than a {cloth}. He went into the jungle and there he found a {organism}! It was {adjective}. In terror he ran into a close village called {village} shouting, "{exclamation}!" The sound of the foot of the {organism} behind him increased with time. The villagers screamed, "It's a {adjective} {organism}!" 
Taking no prisoners the {organism} razed the entire village leaving only the trace of someone's {favourite}.  
Then it went back into the jungle and waited for its next sufferer to appear.'''

    zh.geometry(newGeometry='375x700')

    Label(zh, text='Your Story:', font=("Raleway", 13, "bold"), wraplength=zh.winfo_width(), bg='#0036e6').place(x=130, y=335)
    Label(zh, text=text, font=("Raleway", 13), wraplength=zh.winfo_width(), bg='#0036e6').place(x=0, y=360)

  frame2 = Toplevel(win, bg='#0036e6')
  frame2.title("One Dark, Stormy Night")
  frame2.geometry('375x600')
  frame2.resizable(False, False)

  Label(frame2, text='One Dark, Stormy Night - Mad Libs', font=("Raleway", 17, 'bold'), bg='#0036e6').place(
    x=10, y=0)

  Label(frame2, text='A child\'s name:', font=("Raleway", 16), bg='#0036e6').place(x=0, y=35)
  Label(frame2, text='An article of clothing:', font=("Raleway", 16), bg='#0036e6').place(x=0, y=70)
  Label(frame2, text='A creature:', font=("Raleway", 16), bg='#0036e6').place(x=0, y=110)
  Label(frame2, text='An adjective:', font=("Raleway", 16), bg='#0036e6').place(x=0, y=150)
  Label(frame2, text='A village name:', font=("Raleway", 16), bg='#0036e6').place(x=0, y=190)
  Label(frame2, text='An exclamation:', font=("Raleway", 16), bg='#0036e6').place(x=0, y=230)
  Label(frame2, text='A favorite thing for yours:', font=("Raleway", 16), bg='#0036e6').place(x=0, y=270)
  child_name_entry = Entry(frame2, width=19)
  child_name_entry.place(x=255, y=35)

  textile_entry = Entry(frame2, width=19)
  textile_entry.place(x=255, y=70)

  organism_entry = Entry(frame2, width=19)
  organism_entry.place(x=255, y=110)

  adjective_entry = Entry(frame2, width=19)
  adjective_entry.place(x=255, y=150)

  city_entry = Entry(frame2, width=19)
  city_entry.place(x=255, y=190)

  cry_entry = Entry(frame2, width=19)
  cry_entry.place(x=255, y=230)

  favourite_entry = Entry(frame2, width=19)
  favourite_entry.place(x=255, y=270)

  enter_button = Button(frame2, text="Submit", background="#0036e6", font=('Raleway', 12), command=lambda: final_madlib(frame2, child_name_entry.get(), textile_entry.get(), organism_entry.get(), adjective_entry.get(), city_entry.get(), cry_entry.get(), favourite_entry.get()))
  enter_button.place(x=150, y=300)

  frame2.mainloop()
def third_madlib(win):
  def final_madlib(zh: Toplevel, boy1, boy2, girl1, girl2, beast, exclamation):
    text = f'''
Once upon a time there were two people, {girl1} and {boy1}, walking in the park. They were talking about his {beast}. Then
{boy1} cried, "{exclamation}!" "What is it, {boy1}?" cried {girl1}. "I just recalled one thing, I actually have this 
ring in my pocket." aforesaid {boy1}. "Why would you have that?" asked {girl1}. "Will you marry me?" {boy1} asked. 
{girl1} replied, "Ummmmmmm... Yes, I Love You, {boy1}!" in order that they left on {boy1}'s {beast} to their kingdom and had two 
children named {girl2} and {boy2} and they lived blithely ever after as every story ought to end!'''

    zh.geometry(newGeometry='375x700')

    Label(zh, text='Your Story:', font=("Raleway", 13, "bold"), wraplength=zh.winfo_width(), bg='#FF8C00').place(x=130, y=335)
    Label(zh, text=text, font=("Raleway", 13), wraplength=zh.winfo_width(), bg='#FF8C00').place(x=0, y=360)

  frame3 = Toplevel(win, bg='#FF8C00')
  frame3.title("One Dark, Stormy Night")
  frame3.geometry('375x600')
  frame3.resizable(False, False)

  Label(frame3, text='One Dark, Stormy Night - Mad Libs', font=("Raleway", 17, 'bold'), bg='#FF8C00').place(
    x=10, y=0)

  Label(frame3, text='A boy\'s name:', font=("Raleway", 16), bg='#FF8C00').place(x=0, y=35)
  Label(frame3, text='Another boy\'s name:', font=("Raleway", 16), bg='#FF8C00').place(x=0, y=70)
  Label(frame3, text='A girl\'s name:', font=("Raleway", 16), bg='#FF8C00').place(x=0, y=110)
  Label(frame3, text='Another girl\'s name:', font=("Raleway", 16), bg='#FF8C00').place(x=0, y=150)
  Label(frame3, text='An animal:', font=("Raleway", 16), bg='#FF8C00').place(x=0, y=190)
  Label(frame3, text='An exclamation:', font=("Raleway", 16), bg='#FF8C00').place(x=0, y=230)

 
  boy1_name_entry = Entry(frame3, width=19)
  boy1_name_entry.place(x=255, y=35)

  boy2_name_entry = Entry(frame3, width=19)
  boy2_name_entry.place(x=255, y=70)

  girl1_name_entry = Entry(frame3, width=19)
  girl1_name_entry.place(x=255, y=110)

  girl2_name_entry = Entry(frame3, width=19)
  girl2_name_entry.place(x=255, y=150)

  animal_entry = Entry(frame3, width=19)
  animal_entry.place(x=255, y=190)

  cry_entry = Entry(frame3, width=19)
  cry_entry.place(x=255, y=230)

  enter_button = Button(frame3, text="Submit", background="SteelBlue", font=('Raleway', 12), command=lambda: final_madlib(frame3, boy1_name_entry.get(), boy2_name_entry.get(), girl1_name_entry.get(), girl2_name_entry.get(), animal_entry.get(), cry_entry.get()))
  enter_button.place(x=150, y=300)

  frame3.mainloop()
  base.update()
base.mainloop()
