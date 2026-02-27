

class FinanBot:
    def aviso_padrao(self, texto):
        aviso = (
            "\n\n⚠️ Aviso Importante:\n"
            "- Todo investimento envolve riscos, incluindo possibilidade de perdas.\n"
            "- O FinanBot tem caráter apenas educativo e informativo.\n"
            "- Para orientações práticas e personalizadas, consulte sempre um assessor de investimentos."
        )
        return texto + aviso

    def explicar_financas(self, pergunta):
        
        if pergunta == "cdb":
            return (
                "Passo 1: O CDB (Certificado de Depósito Bancário) é um título emitido por bancos.\n"
                "Passo 2: Funciona como um empréstimo que você faz ao banco.\n"
                "Passo 3: Em troca, você recebe juros sobre o valor aplicado.\n\n"
                "📌 Resumo rápido:\n"
                "- Segurança: protegido pelo FGC até certo limite.\n"
                "- Rentabilidade: pode ser prefixado ou pós-fixado.\n"
                "- Liquidez: varia conforme o contrato."
            )

        elif pergunta == "perfil conservador" or pergunta == "conservador":
            return (
                "Passo 1: O perfil conservador busca segurança e baixa volatilidade.\n"
                "Passo 2: Prioriza ativos com menor risco, mesmo que a rentabilidade seja menor.\n"
                "Passo 3: Prefere liquidez e previsibilidade.\n\n"
                "📌 Resumo rápido:\n"
                "- Conservador = segurança em primeiro lugar.\n"
                "- Ativos comuns: CDB, Tesouro Direto, LCI, LCA, Poupança.\n"
                "- Ideal para quem não quer correr riscos."
            )

        # ... demais ativos e perfis seguem o mesmo padrão (sem aviso aqui)

        else:
            return "Não encontrei explicação para esse termo. Digite 'ajuda' para instruções."

    def iniciar(self):
        print("Olá! Eu sou o FinanBot.")
        escolha = input("Você deseja aprender sobre finanças de forma 'local' ou 'online'? ").lower()

        if escolha in ["local", "online"]:
            print("\n⚠️ Aviso Importante:\n"
                  "- Todo investimento envolve riscos, incluindo possibilidade de perdas.\n"
                  "- O FinanBot tem caráter apenas educativo e informativo.\n"
                  "- Para orientações práticas e personalizadas, consulte sempre um assessor de investimentos.\n")

            print("📌 Categorias de ativos e perfis disponíveis:\n")

            print("🔹 Renda Fixa:\n"
                  "- CDB\n"
                  "- Tesouro Direto\n"
                  "- LCI\n"
                  "- LCA\n"
                  "- Poupança\n"
                  "- Debêntures\n")

            print("🔹 Renda Variável:\n"
                  "- Ações\n"
                  "- Fundos Imobiliários (FIIs)\n"
                  "- ETFs\n"
                  "- Criptomoedas\n")

            print("🔹 Fundos de Investimento:\n"
                  "- Fundos de Renda Fixa\n"
                  "- Fundos de Ações\n"
                  "- Fundos Multimercado\n")

            print("🔹 Previdência Privada:\n"
                  "- Previdência PGBL\n"
                  "- Previdência VGBL\n")

            print("🔹 Perfis de Investidor:\n"
                  "- Perfil Conservador\n"
                  "- Perfil Moderado\n"
                  "- Perfil Arrojado\n")

            print("\nDigite o nome de um ativo ou perfil para receber a explicação.\n"
                  "Digite 'ajuda' para instruções ou 'sair' para encerrar.\n")

            while True:
                pergunta = input("Digite o ativo, perfil ou 'sair': ").lower()
                if pergunta == "sair":
                    print("Encerrando FinanBot. Até logo!")
                    break
                resposta = self.explicar_financas(pergunta)
                print(self.aviso_padrao(resposta))

        else:
            print("Opção inválida. Digite 'local' ou 'online'.")
    def explicar_financas(self, pergunta):
        pergunta = pergunta.strip().lower()

        if pergunta == "cdb":
            return (
                "Passo 1: O CDB é um título emitido por bancos.\n"
                "Passo 2: Ao investir, você empresta dinheiro ao banco.\n"
                "Passo 3: Em troca, o banco paga juros.\n"
                "Passo 4: Existe garantia do FGC até um certo limite.\n"
                "Passo 5: É considerado renda fixa.\n\n"
                "📌 Resumo rápido:\n"
                "- Renda fixa emitida por bancos.\n"
                "- Proteção do FGC.\n"
                "- Pode ter carência.\n"
                "- Rentabilidade superior à poupança."
            )
        elif pergunta == "ações":
            return (
                "Passo 1: Ações representam pequenas partes de uma empresa.\n"
                "Passo 2: Quem compra ações se torna sócio da companhia.\n"
                "Passo 3: O valor das ações varia conforme o mercado.\n"
                "Passo 4: Podem gerar ganhos por valorização ou dividendos.\n"
                "Passo 5: São ativos de renda variável.\n\n"
                "📌 Resumo rápido:\n"
                "- Ações = partes de empresas.\n"
                "- Podem gerar valorização e dividendos.\n"
                "- São renda variável.\n"
                "- Exigem perfil tolerante a risco."
            )
        elif pergunta == "fii" or pergunta == "fundos imobiliários":
            return (
                "Passo 1: FIIs são fundos que investem em imóveis.\n"
                "Passo 2: O investidor compra cotas do fundo.\n"
                "Passo 3: Os rendimentos vêm de aluguéis ou valorização.\n"
                "Passo 4: São negociados em bolsa.\n"
                "Passo 5: São renda variável.\n\n"
                "📌 Resumo rápido:\n"
                "- FIIs = fundos de imóveis.\n"
                "- Podem gerar rendimentos.\n"
                "- São renda variável."
            )
        elif pergunta == "tesouro" or pergunta == "tesouro direto":
            return (
                "Passo 1: O Tesouro Direto é um programa do governo.\n"
                "Passo 2: Você empresta dinheiro ao governo.\n"
                "Passo 3: Existem títulos prefixados, Selic e IPCA.\n"
                "Passo 4: É renda fixa.\n"
                "Passo 5: É muito seguro.\n\n"
                "📌 Resumo rápido:\n"
                "- Tesouro = títulos públicos.\n"
                "- Segurança elevada.\n"
                "- Ideal para conservadores."
            )
        elif pergunta == "fgc" or pergunta == "fundo garantidor":
            return (
                "Passo 1: O FGC protege investidores.\n"
                "Passo 2: Garante até um limite por CPF.\n"
                "Passo 3: Vale para CDB, LCI, LCA, poupança.\n"
                "Passo 4: Se o banco quebrar, devolve o dinheiro.\n\n"
                "📌 Resumo rápido:\n"
                "- FGC = proteção ao investidor.\n"
                "- Garante até um limite.\n"
                "- Segurança extra em renda fixa."
            )
        elif pergunta == "debêntures":
            return (
                "Passo 1: Debêntures são títulos de dívida de empresas.\n"
                "Passo 2: Você empresta dinheiro à companhia.\n"
                "Passo 3: Recebe juros.\n"
                "Passo 4: Não têm FGC.\n\n"
                "📌 Resumo rápido:\n"
                "- Debêntures = dívida de empresas.\n"
                "- Podem render mais.\n"
                "- Sem FGC.\n"
                "- Exigem análise de risco."
            )
        elif pergunta == "lci":
            return (
                "Passo 1: LCI é a Letra de Crédito Imobiliário.\n"
                "Passo 2: Emitida por bancos para financiar imóveis.\n"
                "Passo 3: Isenta de IR para pessoa física.\n"
                "Passo 4: Tem FGC.\n\n"
                "📌 Resumo rápido:\n"
                "- LCI = crédito imobiliário.\n"
                "- Isento de IR.\n"
                "- Proteção do FGC."
            )
        elif pergunta == "lca":
            return (
                "Passo 1: LCA é a Letra de Crédito do Agronegócio.\n"
                "Passo 2: Emitida por bancos para financiar o setor agrícola.\n"
                "Passo 3: Isenta de IR para pessoa física.\n"
                "Passo 4: Tem FGC.\n\n"
                "📌 Resumo rápido:\n"
                "- LCA = crédito agrícola.\n"
                "- Isento de IR.\n"
                "- Proteção do FGC."
            )
        elif pergunta == "poupança":
            return (
                "Passo 1: A poupança é a forma mais tradicional de guardar dinheiro.\n"
                "Passo 2: Tem liquidez imediata.\n"
                "Passo 3: Proteção do FGC.\n\n"
                "📌 Resumo rápido:\n"
                "- Poupança = simples.\n"
                "- Liquidez imediata.\n"
                "- Proteção do FGC.\n"
                "- Rentabilidade baixa."
            )
        elif pergunta == "etf" or pergunta == "etfs":
            return (
                "Passo 1: ETFs (Fundos de Índice) replicam o desempenho de um índice.\n"
                "Passo 2: São negociados em bolsa como ações.\n"
                "Passo 3: Permitem diversificação automática.\n\n"
                "📌 Resumo rápido:\n"
                "- ETFs = fundos que seguem índices.\n"
                "- Negociados em bolsa.\n"
                "- Boa opção para diversificação."
            )
        elif pergunta == "criptomoedas" or pergunta == "cripto":
            return (
                "Passo 1: Criptomoedas são moedas digitais baseadas em blockchain.\n"
                "Passo 2: Não são emitidas por governos.\n"
                "Passo 3: São ativos de alta volatilidade.\n\n"
                "📌 Resumo rápido:\n"
                "- Criptomoedas = moedas digitais.\n"
                "- Alta volatilidade.\n"
                "- Não possuem FGC.\n"
                "- Perfil arrojado."
            )
        elif pergunta == "fundos de investimento" or pergunta == "fundos":
            return (
                "📌 Tipos de Fundos de Investimento:\n"
                "- Fundos de Renda Fixa\n"
                "- Fundos de Ações\n"
                "- Fundos Multimercado\n\n"
                "Digite o tipo de fundo para receber a explicação."
            )

        elif pergunta == "fundos de renda fixa" or pergunta == "renda fixa":
            return (
                "Passo 1: Os Fundos de Renda Fixa aplicam em títulos de dívida, como CDBs e Tesouro Direto.\n"
                "Passo 2: São considerados de baixo risco, pois seguem a lógica da renda fixa.\n"
                "Passo 3: Indicados para investidores conservadores ou moderados.\n\n"
                "📌 Resumo rápido:\n"
                "- Segurança e previsibilidade.\n"
                "- Rentabilidade próxima à renda fixa tradicional.\n"
                "- Boa opção para quem busca estabilidade."
            )

        elif pergunta == "fundos de ações" or pergunta == "ações":
            return (
                "Passo 1: Os Fundos de Ações aplicam majoritariamente em ações de empresas.\n"
                "Passo 2: São de maior risco, pois acompanham a volatilidade da bolsa.\n"
                "Passo 3: Indicados para investidores arrojados ou moderados que aceitam oscilações.\n\n"
                "📌 Resumo rápido:\n"
                "- Potencial de alta rentabilidade.\n"
                "- Alta volatilidade.\n"
                "- Ideal para quem busca crescimento no longo prazo."
            )

        elif pergunta == "fundos multimercado" or pergunta == "multimercado":
            return (
                "Passo 1: Os Fundos Multimercado aplicam em diferentes ativos (renda fixa, ações, câmbio, etc).\n"
                "Passo 2: Podem variar em estratégia: conservadora, moderada ou agressiva.\n"
                "Passo 3: Indicados para quem busca diversificação.\n\n"
                "📌 Resumo rápido:\n"
                "- Flexibilidade de estratégias.\n"
                "- Risco e retorno variáveis.\n"
                "- Boa opção para quem quer diversificar a carteira."
            )
        elif pergunta == "previdência" or pergunta == "previdência privada":
            return (
                "Passo 1: Previdência Privada é um investimento de longo prazo.\n"
                "Passo 2: Voltada para aposentadoria.\n"
                "Passo 3: Pode ter benefícios fiscais.\n\n"
                "📌 Resumo rápido:\n"
                "- Previdência = aposentadoria.\n"
                "- Longo prazo.\n"
            )
        elif pergunta == "previdência pgbl" or pergunta == "pgbl":
            return (
                "Passo 1: O PGBL (Plano Gerador de Benefício Livre) é indicado para quem faz a declaração completa do IR.\n"
                "Passo 2: Permite deduzir até 12% da renda bruta anual na base de cálculo do IR.\n"
                "Passo 3: Na hora do resgate, o imposto incide sobre o valor total (contribuições + rendimentos).\n\n"
                "📌 Resumo rápido:\n"
                "- Previdência PGBL = indicado para quem declara IR completo.\n"
                "- Permite dedução de até 12% da renda.\n"
                "- IR sobre o valor total no resgate."
            )

        elif pergunta == "previdência vgbl" or pergunta == "vgbl":
            return (
                "Passo 1: O VGBL (Vida Gerador de Benefício Livre) é indicado para quem faz a declaração simplificada do IR.\n"
                "Passo 2: Não permite dedução na base de cálculo do IR.\n"
                "Passo 3: No resgate, o imposto incide apenas sobre os rendimentos.\n\n"
                "📌 Resumo rápido:\n"
                "- Previdência VGBL = indicado para quem declara IR simplificado.\n"
                "- Não há dedução de até 12%.\n"
                "- IR apenas sobre os rendimentos."
                "- Benefícios fiscais possíveis."  

            )
        elif pergunta == "multimercado macro":
            return (
                "Passo 1: Fundos Multimercado Macro buscam ganhos a partir de cenários econômicos.\n"
                "Passo 2: Investem em diferentes ativos (ações, juros, moedas).\n"
                "Passo 3: Dependem da visão do gestor sobre economia.\n\n"
                "📌 Resumo rápido:\n"
                "- Multimercado Macro = aposta em cenários econômicos.\n"
                "- Diversificação ampla.\n"
                "- Perfil arrojado."
            )
        elif pergunta == "multimercado juros e moedas":
            return (
                "Passo 1: Fundos Multimercado Juros e Moedas focam em renda fixa e câmbio.\n"
                "Passo 2: Buscam ganhos com variação de taxas de juros e moedas.\n"
                "Passo 3: São menos voláteis que os macro.\n\n"
                "📌 Resumo rápido:\n"
                "- Multimercado Juros e Moedas = foco em renda fixa e câmbio.\n"
                "- Menor volatilidade.\n"
                "- Perfil moderado."
            )
        elif pergunta == "multimercado multiestratégia":
            return (
                "Passo 1: Fundos Multimercado Multiestratégia combinam várias abordagens.\n"
                "Passo 2: Podem investir em ações, juros e moedas.\n"
                "Passo 3: Buscam diversificação máxima.\n\n"
                "📌 Resumo rápido:\n"
                "- Multiestratégia = mistura de várias estratégias.\n"
                "- Diversificação ampla.\n"
                "- Perfil moderado a arrojado."
            )

        elif "melhor" in pergunta or "sugestão" in pergunta or "sugestoes" in pergunta:
            return (
                "Não posso indicar qual ativo é melhor ou dar sugestões de investimento.\n"
                "📌 Recomendo que você consulte um assistente de investimentos ou um profissional habilitado,\n"
                "que poderá analisar seu perfil e objetivos financeiros."
            )

        elif (
            "tipos de ativos" in pergunta
            or "ativos disponíveis" in pergunta
            or "lista de ativos" in pergunta
            or pergunta == "ativos"
            or pergunta == "tipos ativos"
            or pergunta == "tipos finanças"
            or pergunta  == "finanças"
        ):
            return (
                "📌 Tipos de ativos que você pode consultar:\n"
                "- CDB\n"
                "- Ações\n"
                "- Fundos Imobiliários (FIIs)\n"
                "- Tesouro Direto\n"
                "- FGC\n"
                "- Debêntures\n"
                "- LCI\n"
                "- LCA\n"
                "- Poupança\n"
                "- ETFs\n"
                "- Criptomoedas\n"
                "- Fundos de Investimento\n"
                "- Previdência Privada\n"
                "   • Previdência PGBL\n"
                "   • Previdência VGBL\n"
                "- Fundos Multimercado\n"
                "   • Macro\n"
                "   • Juros e Moedas\n"
                "   • Multiestratégia\n\n"
                "Digite o nome de um ativo para receber a explicação."
            )
        
        elif (
            pergunta == "perfís"
            or pergunta == "perfis"
            or pergunta == "perfil"
            or pergunta == "tipos de perfis"
            or pergunta == "tipos perfis"
        ):
            return (
                "📌 Perfis de investidor que você pode consultar:\n"
                "- Perfil Conservador\n"
                "- Perfil Moderado\n"
                "- Perfil Arrojado\n\n"
                "Digite o nome de um perfil para receber a explicação."
            )

        
        elif pergunta == "perfil conservador" or pergunta == "conservador" or pergunta == "perfil":
            return (
                "Passo 1: O perfil conservador busca segurança e baixa volatilidade.\n"
                "Passo 2: Prioriza ativos com menor risco, mesmo que a rentabilidade seja menor.\n"
                "Passo 3: Prefere liquidez e previsibilidade.\n\n"
                "📌 Resumo rápido:\n"
                "- Conservador = segurança em primeiro lugar.\n"
                "- Ativos comuns: CDB, Tesouro Direto, LCI, LCA, Poupança.\n"
                "- Ideal para quem não quer correr riscos."
            )

        elif pergunta == "perfil moderado" or pergunta == "moderado":
            return (
                "Passo 1: O perfil moderado busca equilíbrio entre segurança e rentabilidade.\n"
                "Passo 2: Aceita algum risco em troca de retornos melhores.\n"
                "Passo 3: Diversifica entre renda fixa e variável.\n\n"
                "📌 Resumo rápido:\n"
                "- Moderado = equilíbrio entre risco e retorno.\n"
                "- Ativos comuns: CDB, Tesouro, Fundos Multimercado, algumas Ações.\n"
                "- Ideal para quem aceita oscilações moderadas."
            )

        elif pergunta == "perfil arrojado" or pergunta == "arrojado":
            return (
                "Passo 1: O perfil arrojado busca alta rentabilidade e aceita grande risco.\n"
                "Passo 2: Investe em ativos de maior volatilidade.\n"
                "Passo 3: Tem horizonte de longo prazo e tolerância a perdas.\n\n"
                "📌 Resumo rápido:\n"
                "- Arrojado = foco em crescimento e ganhos elevados.\n"
                "- Ativos comuns: Ações, Criptomoedas, Fundos de Ações, Multimercado agressivo.\n"
                "- Ideal para quem suporta grandes oscilações."
            )
        elif pergunta == "ajuda":
            return (
                "📖 Como usar o FinanBot:\n"
                "- Digite 'local' para iniciar a consulta em modo local.\n"
                "- Digite 'online' (ainda em implementação, redireciona para local).\n"
                "- Digite o nome de um ativo para receber explicações (ex.: 'cdb', 'ações', 'tesouro direto').\n"
                "- Para Previdência, você pode usar 'previdência privada', 'previdência pgbl' ou 'previdência vgbl'.\n"
                "- Para ver a lista completa de ativos, digite 'ativos', 'finanças', 'tipos ativos' ou 'tipos de finanças'.\n"
                "- Digite 'sair' para encerrar o programa.\n\n"
                "👉 Dica: sempre use letras minúsculas para facilitar o reconhecimento."
            )
        else:
            return "Esse ativo não existe ou não reconheço essa combinação."
if __name__ == "__main__":
    bot = FinanBot()
    bot.iniciar()