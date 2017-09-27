<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="text" indent="no" encoding="utf-8"/>


<xsl:template match="/">
//
// !!! THIS FILE IS A TEMPLATE, SHOWING HOW YOUR MODEL COULD BE CUSTOMIZED BY CHANGING BODY MODEL PARAMETERS.
// !!! IT IS RECOMMENDED TO COPY THIS FILE INTO YOUR APPLICATION FOLDER OR COPY NECESSARY
// !!! LINES INTO THE MAIN FILE OF YOUR APPLICATION BEFORE INCLUDING "HumanModel.any" !!!  
// !!! PLEASE NOTE THAT SOME OBVIOUS OPTIONS (ON, OFF, etc) ARE NOT SHOWN HERE !!! 
//

<xsl:apply-templates select="anyxdefs/parameter[not(@deprecated='true')]" />
</xsl:template>


<xsl:template match="parameter[not(opt) and (@default='ON' or @default='OFF')]">
<xsl:text>

</xsl:text>
<xsl:call-template name="parameter_header"/>
// Possible values: ON, OFF</xsl:template>

<xsl:template match="parameter[opt]">
<xsl:text>

</xsl:text>
<xsl:call-template name="parameter_header"/>
// Possible values: <xsl:apply-templates select="opt"/>
</xsl:template>

<xsl:template match="parameter[not(opt) and not(@default='ON' or @default='OFF')]">
<xsl:text>

</xsl:text>
<xsl:call-template name="parameter_header"/>
</xsl:template>

<xsl:template match="opt">
<xsl:value-of select="."/><xsl:text>, </xsl:text>
</xsl:template>



<xsl:template name="parameter_header">
<xsl:variable name="type">
                <xsl:choose>
                  <xsl:when test="not(@type)">
                    <xsl:text>#define </xsl:text>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="@type"/><xsl:text> </xsl:text>
                  </xsl:otherwise>
                </xsl:choose>
</xsl:variable>
<xsl:text>
// </xsl:text> <xsl:value-of select="@descr"/>
// <xsl:value-of select="$type"/><xsl:text> </xsl:text><xsl:value-of select="@name"/><xsl:text> </xsl:text><xsl:value-of select="@default"/>
</xsl:template>


</xsl:stylesheet>