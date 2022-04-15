def tag_block(text, classe='success'):
    return f'<div class="{classe}">{text}</div>'


if __name__ == '__main__':
    # Testes Assertions
    assert tag_block('Successfully added!') == \
        '<div class="success">Successfully added!</div>'
    assert tag_block('Impossible to delete!') == \
        '<div class="success">Impossible to delete!</div>'
    print(tag_block('Block'))
