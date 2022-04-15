block_attr = ('block_acesskey', 'block_id')
ul_attr = ('ul_id', 'ul_style')


def filter_attr(informed, supported):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informed.items()
                    if k in supported)


def tag_block(content, *args, classe='success', inline=False, **new_attr):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args, **new_attr)
    attributes = filter_attr(new_attr, block_attr)
    return f'<{tag} {attributes} class="{classe}">{html}</{tag}>'


def tag_list(*itens, **new_attr):
    list = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {filter_attr(new_attr, ul_attr)}>{list}</ul>'


if __name__ == '__main__':
    print(tag_block('Block'))
    print(tag_block('Inline and class!', classe='Info', inline=True))
    print(tag_block('Inline!', inline=True))
    print(tag_block(inline=True, content='inline'))
    print(tag_block('Failed', classe='Error'))
    print(tag_block('Failed', classe='Error'))
    print(tag_block(tag_list('Item 1', 'Item 2'), classe='Info'))
    print(tag_block(tag_list, 'Friday', 'Monday', classe='Info', inline=True))
    print(tag_block(tag_list, 'Item 1', 'Item 2', classe='info',
                    block_acesskey='m', block_id='content', ul_id='list'))
