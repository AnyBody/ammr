<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="text" indent="no" encoding="utf-8"/>

<xsl:template match="/">
#ifdef _BM_PARAM_DEFINED_ 
#undef _BM_PARAM_DEFINED_
#endif

<xsl:apply-templates select="anyxdefs/parameter" />

</xsl:template>

<xsl:template match="parameter">
#ifdef <xsl:value-of select="@name"/>
#ifndef _BM_PARAM_DEFINED_
#define _BM_PARAM_DEFINED_
#endif
#endif
</xsl:template>

</xsl:stylesheet>
