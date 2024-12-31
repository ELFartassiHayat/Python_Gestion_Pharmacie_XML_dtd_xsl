<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:template match="/">
  
    <html>
      <head>
        <title>Gestion de Pharmacie</title>
        <link rel="stylesheet" type="text/css" href="style.css"/>
      </head>
      <body>
        <h2>Gestion de Pharmacie</h2>
        
        <h3>Clients</h3>
        <table border="1">
          <tr>
            <th>ID_Client</th>
            <th>Nom_Client</th>
            <th>Téléphone</th>
          </tr>
          <xsl:for-each select="pharmacie/Client">
            <tr>
              <td><xsl:value-of select="@ID_Client"/></td>
              <td><xsl:value-of select="@Nom_Client"/></td>
              <td><xsl:value-of select="@Telephone"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h3>Fournisseurs</h3>
        <table border="1">
          <tr>
            <th>ID_Fournisseur</th>
            <th>Nom_Fournisseur</th>
            <th>Téléphone</th>
          </tr>
          <xsl:for-each select="pharmacie/Fournisseur">
            <tr>
              <td><xsl:value-of select="@ID_Fournisseur"/></td>
              <td><xsl:value-of select="@Nom_Fournisseur"/></td>
              <td><xsl:value-of select="@Telephone"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h3>Médicaments</h3>
        <table border="1">
          <tr>
            <th>ID_Medicament</th>
            <th>Nom_Medicament</th>
            <th>Prix</th>
            <th>Quantité_Stock</th>
            <th>ID_Fournisseur</th>
          </tr>
          <xsl:for-each select="pharmacie/Medicament">
            <tr>
              <td><xsl:value-of select="@ID_Medicament"/></td>
              <td><xsl:value-of select="@Nom_Medicament"/></td>
              <td><xsl:value-of select="@Prix"/></td>
              <td><xsl:value-of select="@Quantite_Stock"/></td>
              <td><xsl:value-of select="@ID_Fournisseur"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h3>Commandes</h3>
        <table border="1">
          <tr>
            <th>ID_Commande</th>
            <th>Date</th>
            <th>ID_Client</th>
            <th>ID_Medicament</th>
          </tr>
          <xsl:for-each select="pharmacie/Commande">
            <tr>
              <td><xsl:value-of select="@ID_Commande"/></td>
              <td><xsl:value-of select="@Date"/></td>
              <td><xsl:value-of select="@ID_Client"/></td>
              <td><xsl:value-of select="@ID_Medicament"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>