from pyscript import document, display



def add_member(event):
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    if first_name and last_name:
     all_members.add(first_name + "" +last_name)
     document.getElementById("output1").innerHTML = "<br>".join(sorted(all_members))

     document.getElementById("first_name").value = ""
     document.getElementById("last_name").value = ""

# original list
Grade_7 = {'Lea Ramos', 'Fidel Santos', 'Ali Magsaysay', 'Marie Bautista'}
Grade_8 = {'Trisha Aquino', 'Jiana Cruz', 'Angelic Chavoso', 'Paulene Dela Cruz'}
Grade_9 = {'Gabbi Abad', 'Shenna Bayaban', 'Liza Soberano', 'Bianca Garcia'}
Grade_10 = {'Grace Ocampo', 'Zack Medina', 'Julhia Del Luna', 'Atasha Alfonso'}

all_members = Grade_7 | Grade_8 | Grade_9 | Grade_10

members_list = "<br>".join(sorted(all_members))

document.getElementById("output1").innerHTML = members_list



