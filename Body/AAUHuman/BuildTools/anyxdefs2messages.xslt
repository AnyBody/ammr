<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="text" indent="no" encoding="us-ascii"/>

  <xsl:template match="/">
    <xsl:text>//&#10;// !!! THIS IS AN AUTOMATICALLY GENERATED FILE. DO NOT MODIFY IT !!! &#10;//&#10;&#10;</xsl:text>
    <xsl:text>//&#10;</xsl:text>

    <xsl:text>&#10;#if BM_CONFIG_MESSAGES == ON&#10;AnyFolder Messages = {&#10;</xsl:text>

    <xsl:for-each select="anyxdefs/parameter[not(@deprecated)]">
      <xsl:if test="@valuetype!='reference'">

        <xsl:text>// </xsl:text><xsl:value-of select="@descr"/><xsl:text>&#10;</xsl:text>
        <xsl:text>AnyMessage msg_</xsl:text>
        <xsl:value-of select="@name"/>
        <xsl:text> = { TriggerPreProcess = On; Type = MSG_Message; Message = </xsl:text>
        
        <xsl:choose>
          <xsl:when test="@valuetype='float'">
            <xsl:text>strval(</xsl:text>
          </xsl:when>
          <xsl:when test="@valuetype='integer'">
            <xsl:text>strval(</xsl:text>
          </xsl:when>
        </xsl:choose>

        <xsl:value-of select="@name"/>

        <xsl:choose>
          <xsl:when test="@valuetype='float'">
            <xsl:text>, "%5.3f")</xsl:text>
          </xsl:when>
          <xsl:when test="@valuetype='integer'">
            <xsl:text>)</xsl:text>
          </xsl:when>
        </xsl:choose>

        <xsl:text>;};&#10;</xsl:text>
        <xsl:text>&#10;</xsl:text>
      </xsl:if>
    </xsl:for-each>

    <xsl:text>&#10;}; // AnyFolder Messages&#10;#endif&#10;&#10;#if BM_CONFIG_VALUES == ON&#10;AnyFolder Values = {&#10;&#10;</xsl:text>

    <xsl:for-each select="anyxdefs/parameter[not(@deprecated)]">
      <xsl:if test="@valuetype!='reference'">
        <xsl:text>// </xsl:text><xsl:value-of select="@descr"/><xsl:text>&#10;</xsl:text>

        <xsl:choose>
          <xsl:when test="@valuetype='string'">
            <xsl:text>AnyStringVar value_</xsl:text>
          </xsl:when>
          <xsl:when test="@valuetype='float'">
            <xsl:text>AnyFloatVar value_</xsl:text>
          </xsl:when>
          <xsl:when test="@valuetype='integer'">
            <xsl:text>AnyIntVar value_</xsl:text>
          </xsl:when>
        </xsl:choose>
        <xsl:value-of select="@name"/><xsl:text>=</xsl:text>
        <xsl:value-of select="@name"/>
        <xsl:text>;&#10;&#10;</xsl:text>
      </xsl:if>
    </xsl:for-each>
    <xsl:text>&#10;};// AnyFolder Values&#10;#endif&#10;&#10;</xsl:text>
    <xsl:text>&#10;&#10;</xsl:text>
  </xsl:template>

</xsl:stylesheet>
