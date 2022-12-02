import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
spacer = "                                                                                                                                                                                                                    "
healthMaxValue = 10
hungerMaxValue = 10
thirstMaxValue = 10

healthCurrentValue = 7
hungerCurrentValue = 1
thirstCurrentValue = 5

root = customtkinter.CTk()
root.title("7 VS WILD")
root.geometry("900x800")
root.resizable(False, False)

# oberer Frame
topBanner = customtkinter.CTkFrame(master=root, height=240)
topBanner.pack(pady=10, padx=10, fill="both")

health = customtkinter.CTkLabel(master=topBanner, text="  Gesundheit ")
health.grid(row=0, column=0)

healthValueLable = customtkinter.CTkLabel(master=topBanner, text=f"  {healthCurrentValue}/{healthMaxValue}")
healthValueLable.grid(row=0, column=1)

hunger = customtkinter.CTkLabel(master=topBanner, text="  Hunger")
hunger.grid(row=1, column=0, sticky=customtkinter.W)

hungerValueLable = customtkinter.CTkLabel(master=topBanner, text=f"  {hungerCurrentValue}/{hungerMaxValue}")
hungerValueLable.grid(row=1, column=1)

thirst = customtkinter.CTkLabel(master=topBanner, text="  Durst")
thirst.grid(row=2, column=0, sticky=customtkinter.W)

thirstValueLable = customtkinter.CTkLabel(master=topBanner, text=f"  {thirstCurrentValue}/{thirstMaxValue}")
thirstValueLable.grid(row=2, column= 1)

spacerLable = customtkinter.CTkLabel(master=topBanner, text=spacer)
spacerLable.grid(row=0, column=2)

ClockLable = customtkinter.CTkLabel(master=topBanner, text="Uhrzeit")
ClockLable.grid(row=0, column=3)

clock = customtkinter.CTkLabel(master=topBanner, text="  19:55")
clock.grid(row=0, column=4)



#mittlerer Frame
middleBanner = customtkinter.CTkFrame(master=root, height=240)
middleBanner.pack(pady=10, padx=10, fill="x")

event = customtkinter.CTkLabel(master=middleBanner, text="Randome Text")
event.grid()

#unterer Frame
bottomBanner = customtkinter.CTkFrame(master=root, height=240)
bottomBanner.pack(pady=10, padx=10, fill="x")

text1 = "Hallo ihr lieben2.0"

root.mainloop()
