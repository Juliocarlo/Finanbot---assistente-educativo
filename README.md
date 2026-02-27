# Finanbot---assistente-educativo
Projeto de assistente educativo para atender a entrega do curso da trilha Bradesco

# 📘 Memorial do Projeto – FinanBot

## 1. Introdução
O **FinanBot** é um assistente educativo desenvolvido em Python com o objetivo de explicar conceitos básicos de finanças pessoais e investimentos.  
Ele foi criado para rodar localmente, de forma simples e acessível, sem necessidade de bibliotecas externas ou integração com serviços na nuvem.

---

## 2. Objetivos
- Oferecer explicações claras sobre ativos financeiros e perfis de investidores.  
- Garantir que todas as respostas sejam acompanhadas de um **aviso padrão**, reforçando o caráter informativo e não consultivo do projeto.  
- Proporcionar uma experiência interativa via terminal, permitindo que o usuário explore diferentes tópicos.  

---

## 3. Estrutura do Projeto
O projeto foi implementado em Python, organizado em uma classe principal chamada **`FinanBot`**, composta por três funções principais:

- **`aviso_padrao`**: adiciona automaticamente um aviso em todas as respostas.  
- **`explicar_financas`**: fornece explicações sobre ativos e perfis de investidores.  
- **`iniciar`**: gerencia o fluxo de interação com o usuário, exibindo o menu inicial e recebendo entradas.  

---

## 4. Funcionamento
1. O usuário inicia o programa (`python finanbot.py`).  
2. O menu inicial é exibido.  
3. O usuário escolhe um ativo ou perfil.  
4. O FinanBot retorna uma explicação acompanhada do aviso padrão.  

---

## 5. Ambiente de Execução
- Linguagem: **Python 3.x**  
- Editor utilizado: **VS Code** (também testado no CMD e IDLE)  
- Execução:  
  ```bash
  python finanbot.py
