#tentar definir uma função chamada "loginUsuario" que por sua vez, receberá o parametro "perfil"
def loginUsuario(perfil):
    #tentar converter o valor do parametro para minúscula com lower()
    if perfil.lower() == 'admin':
        print('Bem-Vindo, Adiministrador')
    else:
        print('Bem-Vindo, Usuário')
#dizer que a função está passando diferetes valores como parâmetro
loginUsuario('Admin') #deverá tentar imprimir: 'Bem-Vindo,Administrador'
loginUsuario('admin')  #tentar imprimir: 'Bem-Vindo, Administrador'
loginUsuario('User') #tentar imprimir: 'Bem-Vindo, Usuário'
loginUsuario('usuário') #tentpoderá tentar conseguir imprimir: 'Bem-Vindo, Usuário'