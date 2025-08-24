# INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I (Volleyball Manager)

<p align="center">
  <img width="608" height="238" alt="Captura de Tela 2025-08-24 às 05 05 20 1" src="https://github.com/user-attachments/assets/557fb17a-c2b1-41f1-afd7-f1f8a6df1398" />
</p>

## ℹ️ Sobre o Repositório
Repositório contendo o projeto final desenvolvido para a disciplina **INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I** da Universidade Federal de Santa Catarina (UFSC). O sistema implementa um gerenciador de campeonatos de voleibol universitário utilizando Python e conceitos de programação orientada a objetos.

## 🎯 Objetivo Geral
Desenvolver um sistema para gerenciamento de campeonatos de voleibol que permita:
- Cadastro de cursos, alunos, árbitros e equipes
- Registro de partidas e cálculo automático de pontuações
- Geração de relatórios e estatísticas do campeonato
- Implementação dos conceitos de POO com arquitetura em camadas
- Persistência de dados com serialização

## 📋 Funcionalidades Principais

### Módulo de Cadastros
- **Cursos**: Cadastro de cursos universitários (código e nome)
- **Alunos**: Gestão de alunos com matrícula, curso, nome, CPF e data de nascimento
- **Árbitros**: Controle de árbitros com registro de partidas realizadas
- **Equipes**: Formação de equipes por curso com vinculação de alunos

### Módulo de Partidas
- Registro completo de partidas com data, equipes participantes e árbitro
- Cálculo automático de pontuações (3 pontos por vitória, 2 pontos para vitórias 3x2)
- Atualização de estatísticas de jogadores e equipes

### Módulo de Campeonato
- Classificação geral das equipes
- Ranking dos maiores pontuadores individuais
- Estatísticas diversas (equipes que mais levaram partidas a 3x2, árbitros mais atuantes)

## 🏗️ Arquitetura do Sistema

### Padrão MVC (Model-View-Controller)
- **Model**: Entidades do sistema (Aluno, Curso, Equipe, Partida, Árbitro)
- **View**: Telas implementadas com PySimpleGUI
- **Controller**: Controladores que gerenciam a lógica de cada módulo

### Camada de Persistência
- DAOs (Data Access Objects) para cada entidade
- Serialização com pickle para armazenamento em arquivos .pkl

### Estrutura de Diretórios
```
├── DAOs/           # Objetos de acesso a dados
├── entidade/       # Classes de entidade do sistema
├── controle/       # Controladores (lógica de negócio)
├── limite/         # Telas (interface gráfica)
├── exceptions/     # Exceções personalizadas
└── main.py         # Arquivo principal
```

## 🛠️ Tecnologias Utilizadas
- **Python 3.8+**
- **PySimpleGUI** para interface gráfica
- **Pickle** para persistência de dados
- **Padrões de Projeto**: MVC, DAO, Singleton

## 📚 Conceitos de POO Aplicados
- Herança e polimorfismo
- Encapsulamento
- Associação, agregação e composição
- Tratamento de exceções
- Persistência de objetos
- Interfaces gráficas

## 👨‍💻 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado
- Biblioteca PySimpleGUI (`pip install PySimpleGUI`)

### Execução
```bash
python main.py
```

## 📖 Referências Bibliográficas
1. **Python 3 for Absolute Beginners** - Hall, Tim; Stacey, J. P. (Apress, 2010)
2. **Python: Para Desenvolvedores** - Borges, Luiz Eduardo (Novatec, 2014)
3. **Pro Python** - Alchin, Marty (Apress, 2010)
4. **Design Patterns** - Gamma, E. et al. (Addison-Wesley, 1995)

## 👨‍🏫 Disciplina
**INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I**  
Universidade Federal de Santa Catarina - Centro Tecnológico  
Departamento de Informática e Estatística

### Professores
- Thaís Bardini Idalino
- Eduardo Camilo Inacio

### Aluno
Jonathan Moraes Pereira (23205205)

*Projeto acadêmico desenvolvido para fins educacionais - UFSC 2024*
