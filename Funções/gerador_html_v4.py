def tag_block(content, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_list(*itens):
    list = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{list}</ul>'


if __name__ == '__main__':
    print(tag_block('Block'))
    print(tag_block('Inline and class!', classe='Info', inline=True))
    print(tag_block('Inline!', inline=True))
    print(tag_block(inline=True, content='inline'))
    print(tag_block('Failed', classe='Error'))
    print(tag_block('Failed', classe='Error'))
    print(tag_block(tag_list('Item 1', 'Item 2'), classe='Info'))
    print(tag_block(tag_list, 'Friday', 'Monday', classe='Info', inline=True))
