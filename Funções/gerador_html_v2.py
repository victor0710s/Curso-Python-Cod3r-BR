def tag_block(text, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{text}</{tag}>'


if __name__ == '__main__':
    print(tag_block('Block'))
    print(tag_block('Inline and class!', 'Info', True))
    print(tag_block('Inline!', inline=True))
    print(tag_block('Inline!', 'Error'))
