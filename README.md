Carteira de Senhas com PyQt5, MySQL e Criptografia em Python🔐

Estou muito empolgado em compartilhar meu primeiro projeto público, uma aplicação de carteira de senhas desenvolvida utilizando PyQt5 para a interface gráfica, MySQL para o armazenamento de dados e Cryptography para garantir a segurança na manipulação e armazenamento das senhas.

#🖥️ Funcionalidades da Aplicação:

1. Registro de Usuário com Senha Criptografada: 
   - O usuário pode se cadastrar informando nome, login e senha.
   - A senha é criptografada antes de ser armazenada no banco de dados MySQL, utilizando o pacote Cryptography. O método de criptografia utilizado é o Fernet, que garante a integridade e a confidencialidade dos dados.
   
2. Login Seguro: 
   - Para acessar as funcionalidades da carteira de senhas, o usuário precisa se autenticar.
   - A senha inserida no login é comparada à versão criptografada armazenada no banco de dados, sendo descriptografada para validação.

3. Gerenciamento de Senhas:
   - Uma vez logado, o usuário pode cadastrar senhas de diferentes aplicativos, que também são criptografadas antes de serem salvas no banco.
   - As senhas e os aplicativos cadastrados podem ser listados em uma tabela interativa.

4. Exclusão de Senhas:
   - O usuário tem a opção de excluir senhas que não são mais necessárias diretamente da interface. As informações são atualizadas tanto na aplicação quanto no banco de dados.

5. Segurança em Primeiro Lugar:
   - Tanto as senhas dos usuários quanto as senhas dos aplicativos armazenados são criptografadas usando Fernet antes de serem enviadas ao banco de dados, assegurando que os dados sejam armazenados de forma segura.

#🔧 Tecnologias Utilizadas:
- Python com PyQt5 para a criação da interface gráfica.
- MySQL para o armazenamento das informações.
- Cryptography para garantir a criptografia das senhas, oferecendo uma camada adicional de proteção contra possíveis vazamentos.
  
Este é meu primeiro projeto público, e estou muito feliz com o resultado! O objetivo foi implementar uma aplicação de gerenciamento de senhas que ofereça uma experiência de usuário simples e ao mesmo tempo segura. A criptografia é uma das principais preocupações, garantindo que as senhas jamais sejam armazenadas em texto plano.

Estou animado para continuar aprimorando minhas habilidades e desenvolver mais projetos como este!
