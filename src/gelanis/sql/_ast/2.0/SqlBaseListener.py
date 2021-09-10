# Generated from SqlBase.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlBaseParser import SqlBaseParser
else:
    from SqlBaseParser import SqlBaseParser

# This class defines a complete listener for a parse tree produced by SqlBaseParser.
class SqlBaseListener(ParseTreeListener):

    # Enter a parse tree produced by SqlBaseParser#singleStatement.
    def enterSingleStatement(self, ctx:SqlBaseParser.SingleStatementContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleStatement.
    def exitSingleStatement(self, ctx:SqlBaseParser.SingleStatementContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#singleExpression.
    def enterSingleExpression(self, ctx:SqlBaseParser.SingleExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleExpression.
    def exitSingleExpression(self, ctx:SqlBaseParser.SingleExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#singleTableIdentifier.
    def enterSingleTableIdentifier(self, ctx:SqlBaseParser.SingleTableIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleTableIdentifier.
    def exitSingleTableIdentifier(self, ctx:SqlBaseParser.SingleTableIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#singleDataType.
    def enterSingleDataType(self, ctx:SqlBaseParser.SingleDataTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleDataType.
    def exitSingleDataType(self, ctx:SqlBaseParser.SingleDataTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#statementDefault.
    def enterStatementDefault(self, ctx:SqlBaseParser.StatementDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#statementDefault.
    def exitStatementDefault(self, ctx:SqlBaseParser.StatementDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#use.
    def enterUse(self, ctx:SqlBaseParser.UseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#use.
    def exitUse(self, ctx:SqlBaseParser.UseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createDatabase.
    def enterCreateDatabase(self, ctx:SqlBaseParser.CreateDatabaseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createDatabase.
    def exitCreateDatabase(self, ctx:SqlBaseParser.CreateDatabaseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setDatabaseProperties.
    def enterSetDatabaseProperties(self, ctx:SqlBaseParser.SetDatabasePropertiesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setDatabaseProperties.
    def exitSetDatabaseProperties(self, ctx:SqlBaseParser.SetDatabasePropertiesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dropDatabase.
    def enterDropDatabase(self, ctx:SqlBaseParser.DropDatabaseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dropDatabase.
    def exitDropDatabase(self, ctx:SqlBaseParser.DropDatabaseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createTableUsing.
    def enterCreateTableUsing(self, ctx:SqlBaseParser.CreateTableUsingContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createTableUsing.
    def exitCreateTableUsing(self, ctx:SqlBaseParser.CreateTableUsingContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createTable.
    def enterCreateTable(self, ctx:SqlBaseParser.CreateTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createTable.
    def exitCreateTable(self, ctx:SqlBaseParser.CreateTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createTableLike.
    def enterCreateTableLike(self, ctx:SqlBaseParser.CreateTableLikeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createTableLike.
    def exitCreateTableLike(self, ctx:SqlBaseParser.CreateTableLikeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#analyze.
    def enterAnalyze(self, ctx:SqlBaseParser.AnalyzeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#analyze.
    def exitAnalyze(self, ctx:SqlBaseParser.AnalyzeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#renameTable.
    def enterRenameTable(self, ctx:SqlBaseParser.RenameTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#renameTable.
    def exitRenameTable(self, ctx:SqlBaseParser.RenameTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setTableProperties.
    def enterSetTableProperties(self, ctx:SqlBaseParser.SetTablePropertiesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setTableProperties.
    def exitSetTableProperties(self, ctx:SqlBaseParser.SetTablePropertiesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#unsetTableProperties.
    def enterUnsetTableProperties(self, ctx:SqlBaseParser.UnsetTablePropertiesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#unsetTableProperties.
    def exitUnsetTableProperties(self, ctx:SqlBaseParser.UnsetTablePropertiesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setTableSerDe.
    def enterSetTableSerDe(self, ctx:SqlBaseParser.SetTableSerDeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setTableSerDe.
    def exitSetTableSerDe(self, ctx:SqlBaseParser.SetTableSerDeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#addTablePartition.
    def enterAddTablePartition(self, ctx:SqlBaseParser.AddTablePartitionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#addTablePartition.
    def exitAddTablePartition(self, ctx:SqlBaseParser.AddTablePartitionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#renameTablePartition.
    def enterRenameTablePartition(self, ctx:SqlBaseParser.RenameTablePartitionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#renameTablePartition.
    def exitRenameTablePartition(self, ctx:SqlBaseParser.RenameTablePartitionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dropTablePartitions.
    def enterDropTablePartitions(self, ctx:SqlBaseParser.DropTablePartitionsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dropTablePartitions.
    def exitDropTablePartitions(self, ctx:SqlBaseParser.DropTablePartitionsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setTableLocation.
    def enterSetTableLocation(self, ctx:SqlBaseParser.SetTableLocationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setTableLocation.
    def exitSetTableLocation(self, ctx:SqlBaseParser.SetTableLocationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#recoverPartitions.
    def enterRecoverPartitions(self, ctx:SqlBaseParser.RecoverPartitionsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#recoverPartitions.
    def exitRecoverPartitions(self, ctx:SqlBaseParser.RecoverPartitionsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dropTable.
    def enterDropTable(self, ctx:SqlBaseParser.DropTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dropTable.
    def exitDropTable(self, ctx:SqlBaseParser.DropTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createView.
    def enterCreateView(self, ctx:SqlBaseParser.CreateViewContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createView.
    def exitCreateView(self, ctx:SqlBaseParser.CreateViewContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createTempViewUsing.
    def enterCreateTempViewUsing(self, ctx:SqlBaseParser.CreateTempViewUsingContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createTempViewUsing.
    def exitCreateTempViewUsing(self, ctx:SqlBaseParser.CreateTempViewUsingContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#alterViewQuery.
    def enterAlterViewQuery(self, ctx:SqlBaseParser.AlterViewQueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#alterViewQuery.
    def exitAlterViewQuery(self, ctx:SqlBaseParser.AlterViewQueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createFunction.
    def enterCreateFunction(self, ctx:SqlBaseParser.CreateFunctionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createFunction.
    def exitCreateFunction(self, ctx:SqlBaseParser.CreateFunctionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dropFunction.
    def enterDropFunction(self, ctx:SqlBaseParser.DropFunctionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dropFunction.
    def exitDropFunction(self, ctx:SqlBaseParser.DropFunctionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#explain.
    def enterExplain(self, ctx:SqlBaseParser.ExplainContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#explain.
    def exitExplain(self, ctx:SqlBaseParser.ExplainContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showTables.
    def enterShowTables(self, ctx:SqlBaseParser.ShowTablesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showTables.
    def exitShowTables(self, ctx:SqlBaseParser.ShowTablesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showDatabases.
    def enterShowDatabases(self, ctx:SqlBaseParser.ShowDatabasesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showDatabases.
    def exitShowDatabases(self, ctx:SqlBaseParser.ShowDatabasesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showTblProperties.
    def enterShowTblProperties(self, ctx:SqlBaseParser.ShowTblPropertiesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showTblProperties.
    def exitShowTblProperties(self, ctx:SqlBaseParser.ShowTblPropertiesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showColumns.
    def enterShowColumns(self, ctx:SqlBaseParser.ShowColumnsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showColumns.
    def exitShowColumns(self, ctx:SqlBaseParser.ShowColumnsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showPartitions.
    def enterShowPartitions(self, ctx:SqlBaseParser.ShowPartitionsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showPartitions.
    def exitShowPartitions(self, ctx:SqlBaseParser.ShowPartitionsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showFunctions.
    def enterShowFunctions(self, ctx:SqlBaseParser.ShowFunctionsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showFunctions.
    def exitShowFunctions(self, ctx:SqlBaseParser.ShowFunctionsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showCreateTable.
    def enterShowCreateTable(self, ctx:SqlBaseParser.ShowCreateTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showCreateTable.
    def exitShowCreateTable(self, ctx:SqlBaseParser.ShowCreateTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#describeFunction.
    def enterDescribeFunction(self, ctx:SqlBaseParser.DescribeFunctionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#describeFunction.
    def exitDescribeFunction(self, ctx:SqlBaseParser.DescribeFunctionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#describeDatabase.
    def enterDescribeDatabase(self, ctx:SqlBaseParser.DescribeDatabaseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#describeDatabase.
    def exitDescribeDatabase(self, ctx:SqlBaseParser.DescribeDatabaseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#describeTable.
    def enterDescribeTable(self, ctx:SqlBaseParser.DescribeTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#describeTable.
    def exitDescribeTable(self, ctx:SqlBaseParser.DescribeTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#refreshTable.
    def enterRefreshTable(self, ctx:SqlBaseParser.RefreshTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#refreshTable.
    def exitRefreshTable(self, ctx:SqlBaseParser.RefreshTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#refreshResource.
    def enterRefreshResource(self, ctx:SqlBaseParser.RefreshResourceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#refreshResource.
    def exitRefreshResource(self, ctx:SqlBaseParser.RefreshResourceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#cacheTable.
    def enterCacheTable(self, ctx:SqlBaseParser.CacheTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#cacheTable.
    def exitCacheTable(self, ctx:SqlBaseParser.CacheTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#uncacheTable.
    def enterUncacheTable(self, ctx:SqlBaseParser.UncacheTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#uncacheTable.
    def exitUncacheTable(self, ctx:SqlBaseParser.UncacheTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#clearCache.
    def enterClearCache(self, ctx:SqlBaseParser.ClearCacheContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#clearCache.
    def exitClearCache(self, ctx:SqlBaseParser.ClearCacheContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#loadData.
    def enterLoadData(self, ctx:SqlBaseParser.LoadDataContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#loadData.
    def exitLoadData(self, ctx:SqlBaseParser.LoadDataContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#truncateTable.
    def enterTruncateTable(self, ctx:SqlBaseParser.TruncateTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#truncateTable.
    def exitTruncateTable(self, ctx:SqlBaseParser.TruncateTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#repairTable.
    def enterRepairTable(self, ctx:SqlBaseParser.RepairTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#repairTable.
    def exitRepairTable(self, ctx:SqlBaseParser.RepairTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#manageResource.
    def enterManageResource(self, ctx:SqlBaseParser.ManageResourceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#manageResource.
    def exitManageResource(self, ctx:SqlBaseParser.ManageResourceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#failNativeCommand.
    def enterFailNativeCommand(self, ctx:SqlBaseParser.FailNativeCommandContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#failNativeCommand.
    def exitFailNativeCommand(self, ctx:SqlBaseParser.FailNativeCommandContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setConfiguration.
    def enterSetConfiguration(self, ctx:SqlBaseParser.SetConfigurationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setConfiguration.
    def exitSetConfiguration(self, ctx:SqlBaseParser.SetConfigurationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#resetConfiguration.
    def enterResetConfiguration(self, ctx:SqlBaseParser.ResetConfigurationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#resetConfiguration.
    def exitResetConfiguration(self, ctx:SqlBaseParser.ResetConfigurationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#unsupportedHiveNativeCommands.
    def enterUnsupportedHiveNativeCommands(self, ctx:SqlBaseParser.UnsupportedHiveNativeCommandsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#unsupportedHiveNativeCommands.
    def exitUnsupportedHiveNativeCommands(self, ctx:SqlBaseParser.UnsupportedHiveNativeCommandsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createTableHeader.
    def enterCreateTableHeader(self, ctx:SqlBaseParser.CreateTableHeaderContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createTableHeader.
    def exitCreateTableHeader(self, ctx:SqlBaseParser.CreateTableHeaderContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#bucketSpec.
    def enterBucketSpec(self, ctx:SqlBaseParser.BucketSpecContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#bucketSpec.
    def exitBucketSpec(self, ctx:SqlBaseParser.BucketSpecContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#skewSpec.
    def enterSkewSpec(self, ctx:SqlBaseParser.SkewSpecContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#skewSpec.
    def exitSkewSpec(self, ctx:SqlBaseParser.SkewSpecContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#locationSpec.
    def enterLocationSpec(self, ctx:SqlBaseParser.LocationSpecContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#locationSpec.
    def exitLocationSpec(self, ctx:SqlBaseParser.LocationSpecContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#query.
    def enterQuery(self, ctx:SqlBaseParser.QueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#query.
    def exitQuery(self, ctx:SqlBaseParser.QueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#insertInto.
    def enterInsertInto(self, ctx:SqlBaseParser.InsertIntoContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#insertInto.
    def exitInsertInto(self, ctx:SqlBaseParser.InsertIntoContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#partitionSpecLocation.
    def enterPartitionSpecLocation(self, ctx:SqlBaseParser.PartitionSpecLocationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#partitionSpecLocation.
    def exitPartitionSpecLocation(self, ctx:SqlBaseParser.PartitionSpecLocationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#partitionSpec.
    def enterPartitionSpec(self, ctx:SqlBaseParser.PartitionSpecContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#partitionSpec.
    def exitPartitionSpec(self, ctx:SqlBaseParser.PartitionSpecContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#partitionVal.
    def enterPartitionVal(self, ctx:SqlBaseParser.PartitionValContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#partitionVal.
    def exitPartitionVal(self, ctx:SqlBaseParser.PartitionValContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#describeFuncName.
    def enterDescribeFuncName(self, ctx:SqlBaseParser.DescribeFuncNameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#describeFuncName.
    def exitDescribeFuncName(self, ctx:SqlBaseParser.DescribeFuncNameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#describeColName.
    def enterDescribeColName(self, ctx:SqlBaseParser.DescribeColNameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#describeColName.
    def exitDescribeColName(self, ctx:SqlBaseParser.DescribeColNameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#ctes.
    def enterCtes(self, ctx:SqlBaseParser.CtesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#ctes.
    def exitCtes(self, ctx:SqlBaseParser.CtesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#namedQuery.
    def enterNamedQuery(self, ctx:SqlBaseParser.NamedQueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#namedQuery.
    def exitNamedQuery(self, ctx:SqlBaseParser.NamedQueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableProvider.
    def enterTableProvider(self, ctx:SqlBaseParser.TableProviderContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableProvider.
    def exitTableProvider(self, ctx:SqlBaseParser.TableProviderContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tablePropertyList.
    def enterTablePropertyList(self, ctx:SqlBaseParser.TablePropertyListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tablePropertyList.
    def exitTablePropertyList(self, ctx:SqlBaseParser.TablePropertyListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableProperty.
    def enterTableProperty(self, ctx:SqlBaseParser.TablePropertyContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableProperty.
    def exitTableProperty(self, ctx:SqlBaseParser.TablePropertyContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tablePropertyKey.
    def enterTablePropertyKey(self, ctx:SqlBaseParser.TablePropertyKeyContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tablePropertyKey.
    def exitTablePropertyKey(self, ctx:SqlBaseParser.TablePropertyKeyContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#constantList.
    def enterConstantList(self, ctx:SqlBaseParser.ConstantListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#constantList.
    def exitConstantList(self, ctx:SqlBaseParser.ConstantListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nestedConstantList.
    def enterNestedConstantList(self, ctx:SqlBaseParser.NestedConstantListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nestedConstantList.
    def exitNestedConstantList(self, ctx:SqlBaseParser.NestedConstantListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createFileFormat.
    def enterCreateFileFormat(self, ctx:SqlBaseParser.CreateFileFormatContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createFileFormat.
    def exitCreateFileFormat(self, ctx:SqlBaseParser.CreateFileFormatContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableFileFormat.
    def enterTableFileFormat(self, ctx:SqlBaseParser.TableFileFormatContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableFileFormat.
    def exitTableFileFormat(self, ctx:SqlBaseParser.TableFileFormatContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#genericFileFormat.
    def enterGenericFileFormat(self, ctx:SqlBaseParser.GenericFileFormatContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#genericFileFormat.
    def exitGenericFileFormat(self, ctx:SqlBaseParser.GenericFileFormatContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#storageHandler.
    def enterStorageHandler(self, ctx:SqlBaseParser.StorageHandlerContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#storageHandler.
    def exitStorageHandler(self, ctx:SqlBaseParser.StorageHandlerContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#resource.
    def enterResource(self, ctx:SqlBaseParser.ResourceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#resource.
    def exitResource(self, ctx:SqlBaseParser.ResourceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#singleInsertQuery.
    def enterSingleInsertQuery(self, ctx:SqlBaseParser.SingleInsertQueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleInsertQuery.
    def exitSingleInsertQuery(self, ctx:SqlBaseParser.SingleInsertQueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#multiInsertQuery.
    def enterMultiInsertQuery(self, ctx:SqlBaseParser.MultiInsertQueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#multiInsertQuery.
    def exitMultiInsertQuery(self, ctx:SqlBaseParser.MultiInsertQueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#queryOrganization.
    def enterQueryOrganization(self, ctx:SqlBaseParser.QueryOrganizationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#queryOrganization.
    def exitQueryOrganization(self, ctx:SqlBaseParser.QueryOrganizationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#multiInsertQueryBody.
    def enterMultiInsertQueryBody(self, ctx:SqlBaseParser.MultiInsertQueryBodyContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#multiInsertQueryBody.
    def exitMultiInsertQueryBody(self, ctx:SqlBaseParser.MultiInsertQueryBodyContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#queryTermDefault.
    def enterQueryTermDefault(self, ctx:SqlBaseParser.QueryTermDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#queryTermDefault.
    def exitQueryTermDefault(self, ctx:SqlBaseParser.QueryTermDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setOperation.
    def enterSetOperation(self, ctx:SqlBaseParser.SetOperationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setOperation.
    def exitSetOperation(self, ctx:SqlBaseParser.SetOperationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#queryPrimaryDefault.
    def enterQueryPrimaryDefault(self, ctx:SqlBaseParser.QueryPrimaryDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#queryPrimaryDefault.
    def exitQueryPrimaryDefault(self, ctx:SqlBaseParser.QueryPrimaryDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#table.
    def enterTable(self, ctx:SqlBaseParser.TableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#table.
    def exitTable(self, ctx:SqlBaseParser.TableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#inlineTableDefault1.
    def enterInlineTableDefault1(self, ctx:SqlBaseParser.InlineTableDefault1Context):
        pass

    # Exit a parse tree produced by SqlBaseParser#inlineTableDefault1.
    def exitInlineTableDefault1(self, ctx:SqlBaseParser.InlineTableDefault1Context):
        pass


    # Enter a parse tree produced by SqlBaseParser#subquery.
    def enterSubquery(self, ctx:SqlBaseParser.SubqueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subquery.
    def exitSubquery(self, ctx:SqlBaseParser.SubqueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#sortItem.
    def enterSortItem(self, ctx:SqlBaseParser.SortItemContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#sortItem.
    def exitSortItem(self, ctx:SqlBaseParser.SortItemContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#querySpecification.
    def enterQuerySpecification(self, ctx:SqlBaseParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#querySpecification.
    def exitQuerySpecification(self, ctx:SqlBaseParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#fromClause.
    def enterFromClause(self, ctx:SqlBaseParser.FromClauseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#fromClause.
    def exitFromClause(self, ctx:SqlBaseParser.FromClauseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#aggregation.
    def enterAggregation(self, ctx:SqlBaseParser.AggregationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#aggregation.
    def exitAggregation(self, ctx:SqlBaseParser.AggregationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#groupingSet.
    def enterGroupingSet(self, ctx:SqlBaseParser.GroupingSetContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#groupingSet.
    def exitGroupingSet(self, ctx:SqlBaseParser.GroupingSetContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#lateralView.
    def enterLateralView(self, ctx:SqlBaseParser.LateralViewContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#lateralView.
    def exitLateralView(self, ctx:SqlBaseParser.LateralViewContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setQuantifier.
    def enterSetQuantifier(self, ctx:SqlBaseParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setQuantifier.
    def exitSetQuantifier(self, ctx:SqlBaseParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#relation.
    def enterRelation(self, ctx:SqlBaseParser.RelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#relation.
    def exitRelation(self, ctx:SqlBaseParser.RelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinRelation.
    def enterJoinRelation(self, ctx:SqlBaseParser.JoinRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinRelation.
    def exitJoinRelation(self, ctx:SqlBaseParser.JoinRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinType.
    def enterJoinType(self, ctx:SqlBaseParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinType.
    def exitJoinType(self, ctx:SqlBaseParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinCriteria.
    def enterJoinCriteria(self, ctx:SqlBaseParser.JoinCriteriaContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinCriteria.
    def exitJoinCriteria(self, ctx:SqlBaseParser.JoinCriteriaContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#sample.
    def enterSample(self, ctx:SqlBaseParser.SampleContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#sample.
    def exitSample(self, ctx:SqlBaseParser.SampleContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#identifierList.
    def enterIdentifierList(self, ctx:SqlBaseParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#identifierList.
    def exitIdentifierList(self, ctx:SqlBaseParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#identifierSeq.
    def enterIdentifierSeq(self, ctx:SqlBaseParser.IdentifierSeqContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#identifierSeq.
    def exitIdentifierSeq(self, ctx:SqlBaseParser.IdentifierSeqContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#orderedIdentifierList.
    def enterOrderedIdentifierList(self, ctx:SqlBaseParser.OrderedIdentifierListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#orderedIdentifierList.
    def exitOrderedIdentifierList(self, ctx:SqlBaseParser.OrderedIdentifierListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#orderedIdentifier.
    def enterOrderedIdentifier(self, ctx:SqlBaseParser.OrderedIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#orderedIdentifier.
    def exitOrderedIdentifier(self, ctx:SqlBaseParser.OrderedIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#identifierCommentList.
    def enterIdentifierCommentList(self, ctx:SqlBaseParser.IdentifierCommentListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#identifierCommentList.
    def exitIdentifierCommentList(self, ctx:SqlBaseParser.IdentifierCommentListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#identifierComment.
    def enterIdentifierComment(self, ctx:SqlBaseParser.IdentifierCommentContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#identifierComment.
    def exitIdentifierComment(self, ctx:SqlBaseParser.IdentifierCommentContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableName.
    def enterTableName(self, ctx:SqlBaseParser.TableNameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableName.
    def exitTableName(self, ctx:SqlBaseParser.TableNameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#aliasedQuery.
    def enterAliasedQuery(self, ctx:SqlBaseParser.AliasedQueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#aliasedQuery.
    def exitAliasedQuery(self, ctx:SqlBaseParser.AliasedQueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#aliasedRelation.
    def enterAliasedRelation(self, ctx:SqlBaseParser.AliasedRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#aliasedRelation.
    def exitAliasedRelation(self, ctx:SqlBaseParser.AliasedRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#inlineTableDefault2.
    def enterInlineTableDefault2(self, ctx:SqlBaseParser.InlineTableDefault2Context):
        pass

    # Exit a parse tree produced by SqlBaseParser#inlineTableDefault2.
    def exitInlineTableDefault2(self, ctx:SqlBaseParser.InlineTableDefault2Context):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableValuedFunction.
    def enterTableValuedFunction(self, ctx:SqlBaseParser.TableValuedFunctionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableValuedFunction.
    def exitTableValuedFunction(self, ctx:SqlBaseParser.TableValuedFunctionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#inlineTable.
    def enterInlineTable(self, ctx:SqlBaseParser.InlineTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#inlineTable.
    def exitInlineTable(self, ctx:SqlBaseParser.InlineTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#rowFormatSerde.
    def enterRowFormatSerde(self, ctx:SqlBaseParser.RowFormatSerdeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#rowFormatSerde.
    def exitRowFormatSerde(self, ctx:SqlBaseParser.RowFormatSerdeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#rowFormatDelimited.
    def enterRowFormatDelimited(self, ctx:SqlBaseParser.RowFormatDelimitedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#rowFormatDelimited.
    def exitRowFormatDelimited(self, ctx:SqlBaseParser.RowFormatDelimitedContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableIdentifier.
    def enterTableIdentifier(self, ctx:SqlBaseParser.TableIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableIdentifier.
    def exitTableIdentifier(self, ctx:SqlBaseParser.TableIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#namedExpression.
    def enterNamedExpression(self, ctx:SqlBaseParser.NamedExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#namedExpression.
    def exitNamedExpression(self, ctx:SqlBaseParser.NamedExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#namedExpressionSeq.
    def enterNamedExpressionSeq(self, ctx:SqlBaseParser.NamedExpressionSeqContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#namedExpressionSeq.
    def exitNamedExpressionSeq(self, ctx:SqlBaseParser.NamedExpressionSeqContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#expression.
    def enterExpression(self, ctx:SqlBaseParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#expression.
    def exitExpression(self, ctx:SqlBaseParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#logicalNot.
    def enterLogicalNot(self, ctx:SqlBaseParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#logicalNot.
    def exitLogicalNot(self, ctx:SqlBaseParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanDefault.
    def enterBooleanDefault(self, ctx:SqlBaseParser.BooleanDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanDefault.
    def exitBooleanDefault(self, ctx:SqlBaseParser.BooleanDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#exists.
    def enterExists(self, ctx:SqlBaseParser.ExistsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#exists.
    def exitExists(self, ctx:SqlBaseParser.ExistsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#logicalBinary.
    def enterLogicalBinary(self, ctx:SqlBaseParser.LogicalBinaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#logicalBinary.
    def exitLogicalBinary(self, ctx:SqlBaseParser.LogicalBinaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#predicated.
    def enterPredicated(self, ctx:SqlBaseParser.PredicatedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#predicated.
    def exitPredicated(self, ctx:SqlBaseParser.PredicatedContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#predicate.
    def enterPredicate(self, ctx:SqlBaseParser.PredicateContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#predicate.
    def exitPredicate(self, ctx:SqlBaseParser.PredicateContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#valueExpressionDefault.
    def enterValueExpressionDefault(self, ctx:SqlBaseParser.ValueExpressionDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#valueExpressionDefault.
    def exitValueExpressionDefault(self, ctx:SqlBaseParser.ValueExpressionDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#comparison.
    def enterComparison(self, ctx:SqlBaseParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#comparison.
    def exitComparison(self, ctx:SqlBaseParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#arithmeticBinary.
    def enterArithmeticBinary(self, ctx:SqlBaseParser.ArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#arithmeticBinary.
    def exitArithmeticBinary(self, ctx:SqlBaseParser.ArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#arithmeticUnary.
    def enterArithmeticUnary(self, ctx:SqlBaseParser.ArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#arithmeticUnary.
    def exitArithmeticUnary(self, ctx:SqlBaseParser.ArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dereference.
    def enterDereference(self, ctx:SqlBaseParser.DereferenceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dereference.
    def exitDereference(self, ctx:SqlBaseParser.DereferenceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#simpleCase.
    def enterSimpleCase(self, ctx:SqlBaseParser.SimpleCaseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#simpleCase.
    def exitSimpleCase(self, ctx:SqlBaseParser.SimpleCaseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#columnReference.
    def enterColumnReference(self, ctx:SqlBaseParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#columnReference.
    def exitColumnReference(self, ctx:SqlBaseParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#rowConstructor.
    def enterRowConstructor(self, ctx:SqlBaseParser.RowConstructorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#rowConstructor.
    def exitRowConstructor(self, ctx:SqlBaseParser.RowConstructorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#star.
    def enterStar(self, ctx:SqlBaseParser.StarContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#star.
    def exitStar(self, ctx:SqlBaseParser.StarContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subscript.
    def enterSubscript(self, ctx:SqlBaseParser.SubscriptContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subscript.
    def exitSubscript(self, ctx:SqlBaseParser.SubscriptContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#timeFunctionCall.
    def enterTimeFunctionCall(self, ctx:SqlBaseParser.TimeFunctionCallContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#timeFunctionCall.
    def exitTimeFunctionCall(self, ctx:SqlBaseParser.TimeFunctionCallContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subqueryExpression.
    def enterSubqueryExpression(self, ctx:SqlBaseParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subqueryExpression.
    def exitSubqueryExpression(self, ctx:SqlBaseParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#cast.
    def enterCast(self, ctx:SqlBaseParser.CastContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#cast.
    def exitCast(self, ctx:SqlBaseParser.CastContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#constantDefault.
    def enterConstantDefault(self, ctx:SqlBaseParser.ConstantDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#constantDefault.
    def exitConstantDefault(self, ctx:SqlBaseParser.ConstantDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:SqlBaseParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:SqlBaseParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#functionCall.
    def enterFunctionCall(self, ctx:SqlBaseParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#functionCall.
    def exitFunctionCall(self, ctx:SqlBaseParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#searchedCase.
    def enterSearchedCase(self, ctx:SqlBaseParser.SearchedCaseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#searchedCase.
    def exitSearchedCase(self, ctx:SqlBaseParser.SearchedCaseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nullLiteral.
    def enterNullLiteral(self, ctx:SqlBaseParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nullLiteral.
    def exitNullLiteral(self, ctx:SqlBaseParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:SqlBaseParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:SqlBaseParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#typeConstructor.
    def enterTypeConstructor(self, ctx:SqlBaseParser.TypeConstructorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#typeConstructor.
    def exitTypeConstructor(self, ctx:SqlBaseParser.TypeConstructorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#numericLiteral.
    def enterNumericLiteral(self, ctx:SqlBaseParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#numericLiteral.
    def exitNumericLiteral(self, ctx:SqlBaseParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SqlBaseParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SqlBaseParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#stringLiteral.
    def enterStringLiteral(self, ctx:SqlBaseParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#stringLiteral.
    def exitStringLiteral(self, ctx:SqlBaseParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:SqlBaseParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:SqlBaseParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:SqlBaseParser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:SqlBaseParser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#predicateOperator.
    def enterPredicateOperator(self, ctx:SqlBaseParser.PredicateOperatorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#predicateOperator.
    def exitPredicateOperator(self, ctx:SqlBaseParser.PredicateOperatorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanValue.
    def enterBooleanValue(self, ctx:SqlBaseParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanValue.
    def exitBooleanValue(self, ctx:SqlBaseParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#interval.
    def enterInterval(self, ctx:SqlBaseParser.IntervalContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#interval.
    def exitInterval(self, ctx:SqlBaseParser.IntervalContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#intervalField.
    def enterIntervalField(self, ctx:SqlBaseParser.IntervalFieldContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#intervalField.
    def exitIntervalField(self, ctx:SqlBaseParser.IntervalFieldContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#intervalValue.
    def enterIntervalValue(self, ctx:SqlBaseParser.IntervalValueContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#intervalValue.
    def exitIntervalValue(self, ctx:SqlBaseParser.IntervalValueContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#complexDataType.
    def enterComplexDataType(self, ctx:SqlBaseParser.ComplexDataTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#complexDataType.
    def exitComplexDataType(self, ctx:SqlBaseParser.ComplexDataTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#primitiveDataType.
    def enterPrimitiveDataType(self, ctx:SqlBaseParser.PrimitiveDataTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#primitiveDataType.
    def exitPrimitiveDataType(self, ctx:SqlBaseParser.PrimitiveDataTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#colTypeList.
    def enterColTypeList(self, ctx:SqlBaseParser.ColTypeListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#colTypeList.
    def exitColTypeList(self, ctx:SqlBaseParser.ColTypeListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#colType.
    def enterColType(self, ctx:SqlBaseParser.ColTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#colType.
    def exitColType(self, ctx:SqlBaseParser.ColTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#whenClause.
    def enterWhenClause(self, ctx:SqlBaseParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#whenClause.
    def exitWhenClause(self, ctx:SqlBaseParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#windows.
    def enterWindows(self, ctx:SqlBaseParser.WindowsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#windows.
    def exitWindows(self, ctx:SqlBaseParser.WindowsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#namedWindow.
    def enterNamedWindow(self, ctx:SqlBaseParser.NamedWindowContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#namedWindow.
    def exitNamedWindow(self, ctx:SqlBaseParser.NamedWindowContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#windowRef.
    def enterWindowRef(self, ctx:SqlBaseParser.WindowRefContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#windowRef.
    def exitWindowRef(self, ctx:SqlBaseParser.WindowRefContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#windowDef.
    def enterWindowDef(self, ctx:SqlBaseParser.WindowDefContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#windowDef.
    def exitWindowDef(self, ctx:SqlBaseParser.WindowDefContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#windowFrame.
    def enterWindowFrame(self, ctx:SqlBaseParser.WindowFrameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#windowFrame.
    def exitWindowFrame(self, ctx:SqlBaseParser.WindowFrameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#frameBound.
    def enterFrameBound(self, ctx:SqlBaseParser.FrameBoundContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#frameBound.
    def exitFrameBound(self, ctx:SqlBaseParser.FrameBoundContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#qualifiedName.
    def enterQualifiedName(self, ctx:SqlBaseParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#qualifiedName.
    def exitQualifiedName(self, ctx:SqlBaseParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#identifier.
    def enterIdentifier(self, ctx:SqlBaseParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#identifier.
    def exitIdentifier(self, ctx:SqlBaseParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#unquotedIdentifier.
    def enterUnquotedIdentifier(self, ctx:SqlBaseParser.UnquotedIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#unquotedIdentifier.
    def exitUnquotedIdentifier(self, ctx:SqlBaseParser.UnquotedIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#quotedIdentifierAlternative.
    def enterQuotedIdentifierAlternative(self, ctx:SqlBaseParser.QuotedIdentifierAlternativeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#quotedIdentifierAlternative.
    def exitQuotedIdentifierAlternative(self, ctx:SqlBaseParser.QuotedIdentifierAlternativeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#quotedIdentifier.
    def enterQuotedIdentifier(self, ctx:SqlBaseParser.QuotedIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#quotedIdentifier.
    def exitQuotedIdentifier(self, ctx:SqlBaseParser.QuotedIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:SqlBaseParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:SqlBaseParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#scientificDecimalLiteral.
    def enterScientificDecimalLiteral(self, ctx:SqlBaseParser.ScientificDecimalLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#scientificDecimalLiteral.
    def exitScientificDecimalLiteral(self, ctx:SqlBaseParser.ScientificDecimalLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:SqlBaseParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:SqlBaseParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#bigIntLiteral.
    def enterBigIntLiteral(self, ctx:SqlBaseParser.BigIntLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#bigIntLiteral.
    def exitBigIntLiteral(self, ctx:SqlBaseParser.BigIntLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#smallIntLiteral.
    def enterSmallIntLiteral(self, ctx:SqlBaseParser.SmallIntLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#smallIntLiteral.
    def exitSmallIntLiteral(self, ctx:SqlBaseParser.SmallIntLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tinyIntLiteral.
    def enterTinyIntLiteral(self, ctx:SqlBaseParser.TinyIntLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tinyIntLiteral.
    def exitTinyIntLiteral(self, ctx:SqlBaseParser.TinyIntLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#doubleLiteral.
    def enterDoubleLiteral(self, ctx:SqlBaseParser.DoubleLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#doubleLiteral.
    def exitDoubleLiteral(self, ctx:SqlBaseParser.DoubleLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#bigDecimalLiteral.
    def enterBigDecimalLiteral(self, ctx:SqlBaseParser.BigDecimalLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#bigDecimalLiteral.
    def exitBigDecimalLiteral(self, ctx:SqlBaseParser.BigDecimalLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nonReserved.
    def enterNonReserved(self, ctx:SqlBaseParser.NonReservedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nonReserved.
    def exitNonReserved(self, ctx:SqlBaseParser.NonReservedContext):
        pass



del SqlBaseParser