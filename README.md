# SIGAAWebScraper

O SIGAAWebScraper é uma ferramenta de web scraping desenvolvida em Python usando a biblioteca Selenium. Ela permite automatizar o processo de acesso às notas no site do SIGAA (Sistema Integrado de Gestão de Atividades Acadêmicas).

## Como Usar

1. Clone este repositório para o seu ambiente local.
2. No arquivo `SIGAAWebScraper.py`, insira suas credenciais de login do SIGAA na função `fazer_login(username, password)`.
3. Utilize os métodos fornecidos pela classe `SIGAAWebScraper` para automatizar o acesso às notas:
   - `acessar_pagina_nota()`: Acessa a página de notas no SIGAA.
   - `obter_nota()`: Retorna as notas disponíveis na página de notas.
   - `fechar_navegador()`: Fecha o navegador.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema, tiver sugestões de melhorias ou quiser adicionar novos recursos, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
