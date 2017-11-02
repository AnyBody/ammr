<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="text" indent="no" encoding="us-ascii"/>

  <xsl:template match="/">
    <xsl:text>//&#10;// !!! THIS IS AN AUTOMATICALLY GENERATED FILE. DO NOT MODIFY IT !!! &#10;//&#10;&#10;</xsl:text>
    <xsl:for-each select="anyxdefs/parameter[@default and not(@deprecated)]">
      <xsl:text>// </xsl:text><xsl:value-of select="@descr"/><xsl:text>&#10;</xsl:text>
      <xsl:text>#ifndef </xsl:text><xsl:value-of select="@name"/><xsl:text>&#10;</xsl:text>
      <xsl:choose>
        <xsl:when test="not(@type)">
          <xsl:text>#define </xsl:text>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="@type"/>
          <xsl:text> </xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:value-of select="@name"/>
      <xsl:text> </xsl:text>
         <xsl:call-template name="string-replace-all">
      	  <xsl:with-param name="text" select="@default" />
          <xsl:with-param name="replace" select="'{br}'" />
          <xsl:with-param name="by" select="''" />
        </xsl:call-template>
	<xsl:text>&#10;</xsl:text>
      <xsl:text>#endif&#10;</xsl:text>
      <xsl:text>&#10;</xsl:text>
    </xsl:for-each>
  </xsl:template>

 <xsl:template name="string-replace-all">
    <xsl:param name="text" />
    <xsl:param name="replace" />
    <xsl:param name="by" />
    <xsl:choose>
      <xsl:when test="contains($text, $replace)">
        <xsl:value-of select="substring-before($text,$replace)" />
        <xsl:value-of select="$by" />
        <xsl:call-template name="string-replace-all">
          <xsl:with-param name="text"
          select="substring-after($text,$replace)" />
          <xsl:with-param name="replace" select="$replace" />
          <xsl:with-param name="by" select="$by" />
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$text" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
