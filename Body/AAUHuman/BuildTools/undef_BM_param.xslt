<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="text" indent="no" encoding="utf-8"/>

<xsl:template match="/">
<xsl:apply-templates select="anyxdefs/parameter" />
</xsl:template>

<xsl:template match="parameter">
<xsl:choose>
 <xsl:when test="not(@type)"> 
 #ifdef <xsl:value-of select="@name"/>
 #undef <xsl:value-of select="@name"/>
 #endif
 </xsl:when>
</xsl:choose>

</xsl:template>

</xsl:stylesheet>
