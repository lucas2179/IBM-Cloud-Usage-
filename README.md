# IBM-Cloud-Usage-

1 - Criar action get-token, em python 3.7 e colar o código "get-token.py"<br>
2 - Criar action get-usage, em python 3.7, e colar o codigo "get-usage.py"<br>
3 - Criar action csv-gen, em python 3.7, e colar o código "csv-gen.py"<br>
4 - Adicionar todas em uma sequence, na ordem de criação<br>
5 - Criar acionador para a sequence, com a entrada do arquivo entrada.json (substituir os campos). <br>

# Acessando a api key da IBM Cloud
1 - No menu gerenciar, clicar em acesso IAM <br>
2 - No menu lateral, selecionar chaves de API do IBM Cloud <br>
3 - Clique em "Criar uma chave de API do IBM Cloud" <br>
4 - De um nome para a mesma, depois, clique em Criar<br>
5 - Copie a Apikey<br>

# Descobrindo o Account Id
1 - No menu gerenciar, clique em "Conta"<br>
2 - No menu lateral, clique em "Configurações da Conta" <br>
3 - Copie o ID da conta <br>

# Endpoint do object storage
1 - vá para o Dashboard do object storage<br>
2 - Selecione o bucket desejado<br>
3 - No menu lateral, clique em configuration<br>
4 - E "Terminais", copie o endpoint Público, acrescentando https:// <br>

#cos apikey e Service Id
1 - No menu lateral, seleione "Credenciais de serviço"<br>
2 - Clique em "Nova Credencial", dê um nome para a credencial, e selecione a função Manager<br>
3 - Clique em incluir<br>
4 - Clique em visualizar credenciais<br>
5 - Copie o campo "apikey"<br>
6 - Para o service id, copie o campo "iam_serviceid_crn"


