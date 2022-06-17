def comments_tree(comments):
    tree_ch = {}
    for comment in comments:
        if comment.to_comment:
            if comment.to_comment not in tree_ch:
                tree_ch[comment.to_comment] = [comment]
            else:
                tree_ch[comment.to_comment] += [comment]

    def tree(parent):
        tree_full[parent] = []
        if parent in tree_ch:
            tree_full[parent] = tree_ch[parent]
            children = tree_ch[parent]
            for child in children:
                tree(child)
        return tree_full

    tree_full = {}

    for comment in comments:
        tree(comment)

    tree_level = {}
    base_level = 0
    for comment in tree_full:
        tree_level[comment] = base_level
    for comment in tree_level:
        for child in tree_full[comment]:
            tree_level[child] = tree_level[comment] + 1

    tree_level_alter = {}
    last = None

    for comment, level in tree_level.items():
        if not last:
            tree_level_alter[comment] = level
            last = level
        else:
            tree_level_alter[comment] = level - last
            last = level

    tree_level_alter_enum = {}
    for i, (k, v) in enumerate(tree_level_alter.items()):
        tree_level_alter_enum[k]= (range(abs(v)), v)

    return tree_level_alter_enum
