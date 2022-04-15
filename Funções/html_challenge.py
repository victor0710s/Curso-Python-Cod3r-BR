def tag(tag, *args, **kwagrs):
    if 'html_class' in kwagrs:
        kwagrs['class'] = kwagrs.pop('html_class')
    attr = ' '.join(f'{k}={v}' for k, v in kwagrs.items())
    inner = ' '.join(args)
    return f'<{tag} {attr}><{inner}/>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )
