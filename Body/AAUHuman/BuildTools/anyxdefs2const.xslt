<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="text" indent="no" encoding="us-ascii"/>

  <xsl:template match="/">
    <xsl:text>//&#10;// !!! THIS IS AN AUTOMATICALLY GENERATED FILE. DO NOT MODIFY IT !!! &#10;//&#10;&#10;#ifndef BM_CONSTANTS_DECLARED&#10;&#10;</xsl:text>
    <xsl:for-each select="anyxdefs/constant">
      <xsl:choose>
        <xsl:when test="not(@type)">
          <xsl:text>#define </xsl:text>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="@type"/><xsl:text> </xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:value-of select="@name"/><xsl:text> </xsl:text><xsl:value-of select="@default"/><xsl:text>&#10;</xsl:text>
      <xsl:text>&#10;</xsl:text>
    </xsl:for-each>
    <xsl:text>#define BM_CONSTANTS_DECLARED&#10;&#10;#endif&#10;&#10;&#10;</xsl:text>
  </xsl:template>

</xsl:stylesheet>
