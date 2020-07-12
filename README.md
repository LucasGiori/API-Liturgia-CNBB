
<br>
<b>API - Liturgia CNBB</b>
<br>
<br>
<br>
<br>

<span align="center">

![](https://img.shields.io/github/last-commit/LucasGiori/API-LITURGIA-CNBB)
![](https://img.shields.io/github/commit-activity/m/LucasGiori/API-LITURGIA-CNBB)
![](https://img.shields.io/github/repo-size/LucasGiori/API-LITURGIA-CNBB)
![](https://img.shields.io/github/languages/count/LucasGiori/API-LITURGIA-CNBB)
![](https://img.shields.io/github/languages/top/LucasGiori/API-LITURGIA-CNBB)

</span>


<br>
<table style="width:100%">
  <tr>
    <th>Rota</th>
    <th>Métodos HTTP Disponíveis</th>
    <th>Parâmetros</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td><code>/api/liturgia</code></td>
    <td align="center">GET | POST</td>
    <td>
        {
          "ano":"2020"
          ,"mes":"07"
          ,"dia":"13"
        }
    </td>
    <td>O método GET desta rota retorna a liturgia da data atual, já o método POST, pode passar parâmetros de Ano,Mês e dia.</td>
  </tr>
  
</table>
<br><br><br>

## :bulb: Imagens de teste realizados no POSTMAN.

- **Método POST**
<br>
<h3 align="center">
    <img 
        alt="Screenshot da aplicação, método POST" 
        title="Screenshot da aplicação, método POST"
        width="800px"
        src="./.github/POST.png"
    >
</h3>

- **Método GET**
<h3 align="center">
<br>
    <img 
        alt="Screenshot da aplicação, método GET" 
        title="Screenshot da aplicação, método GET"
        width="800px"
        src="./.github/GET.png"
    >
</h3>
<br>

- **Requisições do Método POST o Body da requisição deve ser obrigatório application/json.**
<h3 align="center">
    <img 
        alt="Screenshot da aplicação, validação" 
        title="Screenshot da aplicação, Validação"
        width="800px"
        src="./.github/VALIDACAO.png"
    >
</h3>