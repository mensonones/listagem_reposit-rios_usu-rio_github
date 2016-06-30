import requests

#nome do usuário do github para listar os repositórios
name_user = 'mensonones'
response = requests.get('https://api.github.com/users/'+name_user+'/repos')

#requisição ok
assert response.status_code == 200

#printa o nome do usuário do github
print "Usuário:" + name_user + "\n"

#lista os repositórios por linguagem e nome do repositório
for repo in response.json():
    
    print '[{}] {}'.format(repo['language'], repo['name'])
