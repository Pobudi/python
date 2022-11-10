
BG_COLOR = "#9C51E0"

'''
class Setup:

    def __init__(self):
        self.window = Tk()
        self.window.config(bg=BG_COLOR)

        self.cat_listbox = Listbox(height=8)
        self.categories = ["", "", "", "", "", "", "", "Any Category", "General Knowledge", "Entertainment: Books",
                           "Entertainment: Film", "Entertainment: Music", "Entertainment: Musicals & Theatres",
                           "Entertainment: Television", "Entertainment: Video Games", "Entertainment: Board Games",
                           "Science & Nature", "Science: Computers", "Science: Mathematics", "Mythology", "Sports",
                           "Geography", "History", "Politics", "Art", "Celebrities", "Animals", "Vehicles",
                           "Entertainment: Comics", "Science: Gadgets", "Entertainment: Japanese Anime & Manga",
                           "Entertainment: Cartoon & Animations"]

        for category in self.categories[7:]:
            self.cat_listbox.insert(self.categories.index(category), category)
        self.cat_listbox.bind("<<ListboxSelect>>", self.f_categories)
        self.cat_listbox.grid(row=0, column=0)

        self.window.mainloop()

    def f_categories(self, event):
        chosen_cat = self.categories.index(self.cat_listbox.get(self.cat_listbox.curselection()))
        if chosen_cat != "General knowledge":
            data.parameters["category"] = 9
'''
if "":
    print("prwda")