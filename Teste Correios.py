from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("http://www.buscacep.correios.com.br")
    pagina.fill('//*[@id="endereco"]', "69082-640")
    pagina.locator('//*[@id="btn_pesquisar"]').click()

    logradouro = pagina.inner_text('//*[@id="resultado-DNEC"]/tbody/tr/td[1]')
    Bairro_Distrito = pagina.inner_text('//*[@id="resultado-DNEC"]/tbody/tr/td[2]')
    Localidade_UF = pagina.inner_text('//*[@id="resultado-DNEC"]/tbody/tr/td[3]')
    CEP = pagina.inner_text('//*[@id="resultado-DNEC"]/tbody/tr/td[4]')

    pagina.goto("http://www.buscacep.correios.com.br")
    pagina.fill('//*[@id="endereco"]', "Instituto Chreatus")
    pagina.locator('//*[@id="btn_pesquisar"]').click()

    resultado_falha = pagina.inner_text('//*[@id="mensagem-resultado-alerta"]/h6')

    print("O resultado da sua busca por CEP é: %s, %s, %s, %s" % (logradouro, Bairro_Distrito, Localidade_UF, CEP))
    print("O resultado da busca pelo nome 'Instituto Chreatus' é: %s" % resultado_falha)
