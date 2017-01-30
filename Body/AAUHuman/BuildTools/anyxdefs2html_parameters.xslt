<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <html>
      <body>
        <h1>Parameters</h1>
        <table border="1">
          <tr bgcolor="#999999">
            <th>Name</th>
            <th>Description</th>
            <th>Options and Defaults</th>
            <th>Type</th>
          </tr>
          <xsl:for-each select="anyxdefs/parameter">
            <tr>
              <td><i>
                <xsl:value-of select="@name"/>
              </i></td>
              <td>
                <xsl:value-of select="@descr"/>
              </td>
              <td><xsl:for-each select="opt">
                <xsl:value-of select="."/>
		<br/>
              </xsl:for-each>		
              <b>Default:<br/>&#10;
         <xsl:call-template name="string-replace-all">
      	  <xsl:with-param name="text" select="@default" />
          <xsl:with-param name="replace" select="'{br}'" />
        </xsl:call-template>

              </b><br/>
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

 <xsl:template name="string-replace-all">
    <xsl:param name="text" />
    <xsl:param name="replace" />
    <xsl:choose>
      <xsl:when test="contains($text, $replace)">
        <xsl:value-of select="substring-before($text,$replace)" />
        <br/>
        <xsl:call-template name="string-replace-all">
          <xsl:with-param name="text"
          select="substring-after($text,$replace)" />
          <xsl:with-param name="replace" select="$replace" />
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$text" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
