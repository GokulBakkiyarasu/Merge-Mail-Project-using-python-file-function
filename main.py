with open("/Users/admin/PycharmProjects/Mail-Merge-Project/Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
with open("/Users/admin/PycharmProjects/Mail-Merge-Project/Input/Letters/starting_letter.txt") as letter:
    full_letter = letter.readlines()
sender = []
for name in name_list:
    name = name.strip()
    new_txt = full_letter[0].replace("[name]", name)
    sender.append(new_txt)
all_letters = []
for i in range(len(name_list)-1):
    full_letter[0] = sender[i]
    with open(f"/Users/admin/PycharmProjects/Mail-Merge-Project/Output/ReadyToSend/Letters{i+1}.txt", mode="w") as \
            writer:
        for j in range(len(full_letter)):
            writer.write(full_letter[j])