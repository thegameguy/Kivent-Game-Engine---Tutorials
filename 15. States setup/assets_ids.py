objs = ['background',
    'star1', 'star2', 'star3', 'star4', 'star5', 'star6', 'star7', 'star8', 'star9', 'star10', 'star11', 'star12',
    'star13', 'star14', 'star15', 'star16', 'star17', 'star18', 'star19', 'star20', 'star21', 'star22', 'star23',
    'star24', 'star25', 'star26', 'star27', 'star28', 'star29', 'star30', 'star31', 'star32', 'star33', 'star34',
    'star35', 'star36', 'star37', 'star38', 'star39', 'star40', 'star41', 'star42', 'star43', 'star44', 'star45',
    'star46', 'star47', 'star48', 'star49', 'star50',
        'moon', 'ground', 'batholder', 'bat', 'goal', 'youwin', 'start_btn']
num = []
for x in range(len(objs)):
    new = 10571+x
    num.append(new)

ent = {}
for x in range(len(objs)):
    ent[objs[x]] = num[x]
