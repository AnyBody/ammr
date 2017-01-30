<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <html>
      <body>
        <h1>Constants</h1>
        <table border="1">
          <tr bgcolor="#999999">
            <th>Name</th>
            <th>Description</th>
            <th>Value</th>
            <th>Type</th>
          </tr>
          <xsl:for-each select="anyxdefs/constant">
            <tr>
              <td><i>
                <xsl:value-of select="@name"/>
              </i></td>
              <td>
                <xsl:value-of select="@descr"/>
              </td>
              <td>
                <xsl:value-of select="@default"/>
              </td>
              <td>
                <xsl:choose>
                  <xsl:when test="not(@type)">
                    <xsl:text>#define </xsl:text>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="@type"/>
                  </xsl:otherwise>
                </xsl:choose>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
