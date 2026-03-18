Python Cloud SDK wraps Aspose.Words Cloud API so you could seamlessly integrate Microsoft Word® file generation, manipulation, conversion & inspection features into your own python applications.

[Aspose.Words Cloud SDK for Python](https://products.aspose.cloud/words/python) allows to work with Word document headers, footers, page numbering, tables, sections, document comments, drawing objects, FormFields, fonts, hyperlinks, ranges, paragraphs, math objects, watermarks, revisions and document protection. It also assists in appending documents, splitting documents as well as converting document to other supported file formats. Please feel free to explore the [Developer's Guide](https://docs.aspose.cloud/display/wordscloud/Developer+Guide) for all possible usage scenarios. 

## Document Processing Features

- Programmatically create new documents of various file formats.
- Availability of Mail Merge and report generation features.
- Split or merge documents on demand.
- Manage watermarks and protection.
- Full read & write access to Document Object Model.
- Fetch web pages via URL and save in Microsoft Word file formats.
- Get document information in JSON or XML representation.
- [Fetch statistical data](https://docs.aspose.cloud/display/wordscloud/Get+Document+Statistics) of a document.
- [Remove all macros](https://docs.aspose.cloud/display/wordscloud/Remove+all+Macros+from+Document) contained in a specific document.
- [Convert a document to desired file format](https://docs.aspose.cloud/display/wordscloud/Convert+Document+to+Destination+Format+with+Detailed+Settings+and+Save+Result+to+Storage) along with detailed settings.
- Convert an encrypted PDF document into Word document format.

## Enhancements in Version 26.3

- Various stability and performance improvements.


## Enhancements in Version 26.2

- Implemented ability to save documents as Docling JSON format.


## Enhancements in Version 26.1

- Add fontsLocation parameter for Compare API.


## Enhancements in Version 25.12

- Classification API has been removed.


## Enhancements in Version 25.11

- Added 'OfficeMathExportMode' property for TextSaveOptionsData class.
- Added 'ExportFloatingShapesAsInlineTag' property for PdfSaveOptionsData class.


## Enhancements in Version 25.8

- Updated supported version of Python.

## Enhancements in Version 25.6

- Added support for SVG images format in Watermark API.
- Added 'RemoveJavaScriptFromLinks' property for HtmlSaveOptionsData class.


## Enhancements in Version 25.5

- Added data models support for classes 'CommentRangeStart', 'CommentRangeEnd'.
- Added data models support for classes 'FormFieldCheckboxLink', 'FormFieldDropDownLink', 'FormFieldTextInputLink'.


## Enhancements in Version 25.4

- Added 'AttachmentsEmbeddingMode' property for PdfSaveOptionsData class.
- Added 'UpdateAmbiguousTextFont' property for SaveOptionsData class.
- Added 'Granularity' property for CompareOptions class.


## Enhancements in Version 25.2

- Added 'IdPrefix' property for HtmlFixedSaveOptionsData and SvgSaveOptionsData class.


## Enhancements in Version 24.12

- Added 'RenderChoiceFormFieldBorder' property for PdfSaveOptionsData class.
- Added 'ApplySuperscript' property for ReplaceTextParameters class.


## Enhancements in Version 24.11

- Added GetAllRevisions method to obtain all available revisions in document.
- Added AppendAllEntriesToOneSection parameter to AppendDocument method to append entries to the same section.


## Enhancements in Version 24.9

- Added digital signature methds for DOC, DOCX, XPS, or ODT documents.
- Added ReplaceBackslashWithYenSign property for XpsSaveOptions and HtmlSaveOptions.
- Added DigitalSignature property for XpsSaveOptions.
- Added UseSdtTagAsFormFieldName property for PdfSaveOptions.
- Added MergeWholeDocument parameter to the MailMerge operations to update fields in whole document after executing of a mail merge with regions.


## Enhancements in Version 24.8

- Added the support of OpenType standard. It is usefull for languages required advanced typography.


## Enhancements in Version 24.7

- Added support for azw3 (Amazon Kindle Format) documents.
- Added 'MaxImageResolution' property for SvgSaveOptionsData class.


## Enhancements in Version 24.6

- Added the 'TranslateNodeId' method to transalate a node id to a node path.


## Enhancements in Version 24.5

- Added the support of multistorage operations. Saving a file as a result of an operation can be performed in a specific storage, when, used file path in the next format '@storage:path/to/file.doc'.


## Enhancements in Version 24.4

- Added the 'MergeWithNext' method to merge a section with the next one.
- Added the 'LockAspectRatio' propperty for DrawingObjectInsert and DrawingObjectUpdate methods.


## Enhancements in Version 24.3

- Added support for 'RemoveEmptyCells' option for the 'Cleanup' parameter in the insert 'MailMerge' API method.


## Enhancements in Version 24.1

- Added support for InsertAfterNode in the insert API without NodePath.
- Added support for inserting nodes (runs/rows/cells/bookmarks) without NodePath.
- Added support for transparency in the Watermark API.
- Added support for password and encryptedPassword fields in FileReference.
- Fixed missing href value in document responses.


## Enhancements in Version 23.12

- Properties Name, Text, StartRange, EndRange marked as required for InsertBookmark operation.
- Implemented DeleteOfficeMathObjects operation to delete all office math objects from document.
- Parameter ProtectionRequest was removed from the UnprotectDocument operation. Now removing protection from a document does not require a password.
- Model ProtectionRequest marked as deprecated, please use ProtectionRequestV2 instead for perform ProtectDocument operation. To change the password or protection type of protected document, the old password is no required.
- Added fields Password and EncryptedPassword to FileReference for documents encrypted by password.
- Removed parameter encryptedPassword2 from CompareDocument method. Please use FileReference password instead.
- Rename aspose-client header.

## Enhancements in Version 23.11

- Support of required properties in models.
- Property StyleName marked as required for InsertStyle operation.
- Property StyleName marked as required for CopyStyle operation.
- Property StyleName marked as required for ApplyStyleToDocumentElement operation.
- Properties SdtType and Level marked as required for InsertStructuredDocumentTag operation.
- Property Text marked as required for InsertParagraphoperation.
- Property Value marked as required for CreateOrUpdateDocumentProperty operation.
- Property NewValue marked as required for ReplaceText operation.
- Property Text marked as required for ReplaceWithText operation.


## Enhancements in Version 23.9

- Support for class inheritance in responses from the server.


## Enhancements in Version 23.6

- Fix XMLHttpRequest in web applications.


## Enhancements in Version 23.5

- Added InsertSection method.


## Enhancements in Version 23.4

- Added new type of RangeEndIdentifier for RangeApi: document:end


## Enhancements in Version 23.3

- Fix compatibility between CreateDocument API and Dropbox storage.
- Fix compatibility for property PageCount for FixedPageSaveOptionsData.


## Enhancements in Version 23.2

- Added operations to manipulate with Structure Document Tags (SDT) in documents.


## Enhancements in Version 23.1

- Various changes related to stability and performance


## Enhancements in Version 22.12

- Various changes related to stability and performance


## Enhancements in Version 22.11

- Added 'EmbedAttachments' property for PdfSaveOptionsData class.


## Enhancements in Version 22.10

- Added 'CacheHeaderFooterShapes' property for PdfSaveOptionsData class.
- FileReference structure has been added that allows to determine how the document will be accessed: from the remote storage, or loaded directly in the request.
- The 'AppendDocument' and 'AppendDocumentOnline' methods takes a 'FileReference' instead of an 'href' property.
- Added property 'StartingNumber' for 'PageNumbers' class.
- Added property 'GlobalCultureName' for 'FieldOptions' class.


## Enhancements in Version 22.9

- CompressDocument method now can handle images.
- Added support to convert password protected document using ConvertDocument API.


## Enhancements in Version 22.8

- Added optional loadEncoding and password parameters for ConvertDocument API method.


## Enhancements in Version 22.7

- Expand 'AppendDocument' API method to support 'ImageEntryList' for directly appending images to documents and another images.
- Added 'CompressDocument' API method to support compression and resizing images inside the document for reduce the size of the document.


## Enhancements in Version 22.6

- Added 'DeleteBookmark' and 'DeleteBookmarkOnline' API methods for delete bookmarks by name from the document.
- Added 'DeleteBookmarks' and 'DeleteBookmarksOnline' API methods for delete all bookmarks from the document.
- Added 'InsertBookmark' and 'InsertBookmarkOnline' API methods for create new bookmarks in the document.
- Support all save formats for 'CreateDocument' operation.


## Enhancements in Version 22.5

- Internal API fixes and improvments.


## Enhancements in Version 22.4

- Added ExportShapesAsSvg to HtmlSaveOption.
- Added new endpoint '~/styles/copy_from'.


## Enhancements in Version 22.3

- Online methods returns the dictionary of files with included original filename as key instead of single file content in responses.
- Parameters contained sensitive data should be passed in encrypted form. Names of the parameters have 'encrypted' prefix.
- Added Encrypt method to encrypt data on the API public key. Use it to prepare values for parameters required encrypted data.
- Changed type of enumerations for members of SaveOptionsData and other inherited classes from string to enum.


## Enhancements in Version 22.2

- Made 'SaveOprionsData.SaveFormat' property readonly with default value.
- Added subclasses for all formats of SaveOprionsData with specified SaveFormat.
- 'SaveOptionsData', 'FixedPageSaveOptionsData', 'ImageSaveOptionsData', 'OoxmlSaveOptionsData', 'TxtSaveOptionsBaseData' classes now is abstract.


## Enhancements in Version 22.1

- Added 'FieldOptions.FieldUpdateCultureName' to set Culture for fields
- Added 'DocumentEntry.Password' to set an encrypted password for appending document
- Added 'encryptedPassword2' query parameter to CompareDocuments to set an encrypted password for the second comparing document


## Enhancements in Version 21.12

- Added FieldOptions parameter to mail merge operations
- Added timeout parameter to api configuration


## Enhancements in Version 21.11



## Enhancements in Version 21.10

- Removed 'GraphicsQualityOptions' image save option as it no longer supported.
- Added query parameter 'displayIntermediateResults' for batch requests. If 'false', the last response in batch will be returned only. Default is 'true'
- Added 'JsonDataLoadOptions' and 'XmlDataLoadOptions' to 'ReportEngineSettings'


## Enhancements in Version 21.8

- Added new api methods to get, insert, update or delete custom xml parts from documents.
- Added parameter 'ResultDocumentFormat' to Compare API
- Added 'ExportLanguageToSpanTag' pdf save option
- Added 'FlatOpcXmlMappingOnly' save option


## Enhancements in Version 21.7

- ImlRenderingMode option introduced witch is used to determine how ink (InkML) objects are rendered
- MaxCharactersPerLine option introduced which is used to specify the maximum number of characters per one line
- Added new API method to get a RSA public key to encrypt document passwords
- Added encryptedPassword common query option to pass an encrypted document password


## Enhancements in Version 21.6

- Implemented beta version of CompareDocumentOnline feature with both document sending in request
- CompareDocument method now can handle PDF files
- AcceptAllRevisionsBeforeComparison option introduced which is used to specify if accept all revisions before comparison


## Enhancements in Version 21.5

- Update dependencies in sdk


## Enhancements in Version 21.4

- Removed obsolete pdf save option 'EscapeUri'
- SaveOptions now contains CustomTimeZoneInfo to set custom timezone when SdtType.Date structured document tag updated from custom XML
- Url of child requests in batch can be full now (earlier it can be only relative)
- Added 'RquestId' header to all responses


## Enhancements in Version 21.3

- Added 'UpdateCreatedTimeProperty' save option
- Added Tables into HeaderFooter so it's possible to address paragraphs inside table which is located in headerfooter (sections/0/headersfooters/1/tables/0/rows/0/cells/0/paragraphs/0)


## Enhancements in Version 21.2

- Added delete all comments method


## Enhancements in Version 21.1

- Added online version for all API methods


## Enhancements in Version 20.11

- In configuration json file appSid / appKey has been replaced to clientId / clientSecret.
- In Words API initialization methods clientId parameter precedes clientSecret parameter.


## Enhancements in Version 20.10

- Internal API changes.


## Enhancements in Version 20.9

- Added Batch API feature


## Enhancements in Version 20.8

- Added new api method (PUT '/words/{name}/compatibility/optimize') which is allows to optimize the document contents as well as default Aspose.Words behavior to a particular versions of MS Word
- Added 'ApplyBaseDocumentHeadersAndFootersToAppendingDocuments' option to 'DocumentEntryList' for AppendDocument API
- WithoutNodePath methods have been removed, pass null values instead


## Enhancements in Version 20.7

- Added 'Markdown' save format
- Added endpoint to update paragraph format without node path (PUT '/words/{name}/paragraphs/{index}/format')


## Enhancements in Version 20.6

- Added new methods:
  - DeleteAllParagraphTabStopsWithoutNodePath
  - DeleteParagraphTabStopWithoutNodePath
  - GetParagraphTabStopsWithoutNodePath
  - InsertOrUpdateParagraphTabStopWithoutNodePath
  - InsertParagraphWithoutNodePath
  - UpdateParagraphFormatWithoutNodePath
  - UpdateParagraphListFormatWithoutNodePath
  - DeleteParagraphListFormatWithoutNodePath
- DrawingObject related methods have been changed body content. Special request classes are introduced instead of strings.
- InsertOrUpdateParagraphTabStop, DeleteParagraphTabStop methods have been changed parameter order
- OoxmlSaveOptionsData.CompressionLevel property has been added


## Enhancements in Version 20.5

- Added methods to work with Word document lists
  - GetLists
  - GetList
  - InsertList
  - UpdateList
  - UpdateListLevel
- Added methods to work with styles
  - GetStyles
  - UpdateStyle
  - InsertStyle
  - CopyStyle
  - GetStyleFromDocumentElement
  - ApplyStyleToDocumentElement
- Added methods to work with paragraph list format
  - GetParagraphListFormat
  - GetParagraphListFormatWithoutNodePath
  - UpdateParagraphListFormat
  - DeleteParagraphListFormat
- Added methods to work with paragraph tab stops
  - GetParagraphTabStops
  - InsertOrUpdateParagraphTabStop
  - DeleteAllParagraphTabStops
  - DeleteParagraphTabStop
- Added methods to build reports
  - BuildReport
  - BuildReportOnline
- Added Shading property to ParagraphFormat


## Read & Write Document Formats

**Microsoft Word:** DOC, DOCX, RTF, DOT, DOTX, DOTM, FlatOPC (XML)
**OpenOffice:** ODT, OTT
**WordprocessingML:** XML
**Web:** HTML, MHTML, HtmlFixed
**Text:** TXT
**Fixed Layout:** PDF

## Save Document As

**Fixed Layout:** PDF/A, XPS, OpenXPS, PS
**Images:** JPEG, PNG, BMP, SVG, TIFF, EMF
**Others:** PCL

## Platform Independence

Aspose.Words Cloud’s platform independent document manipulation API is a true REST API that can be used from any platform. You can use it with any language or platform that supports REST, be it the web, desktop, mobile, or the cloud. The API integrates with other cloud services to provide you the flexibility you require for processing documents. It is suitable for the most types of businesses, documents, or content.

## Getting Started with Aspose.Words Cloud SDK for Python

Firstly, create an account at [Aspose for Cloud](https://dashboard.aspose.cloud/#/apps) to get your application information and free quota to use the API. Now execute `pip install aspose-words-cloud` from the command line to fetch the SDK. Then import the package via `import asposewordscloud`. 

### Install via Setuptools

Execute `python setup.py install --user` and import the package as `import asposewordscloud`.

The complete source code is available at [GitHub Repository](https://github.com/aspose-words-cloud/Aspose.Words-Cloud-SDK-for-Python).

## Delete Watermarks from Word Document via Python

```python
        # Start README example

        self.words_api = asposewordscloud.WordsApi(client_id, client_secret, base_url)

        upload_request = asposewordscloud.models.requests.UploadFileRequest(
            open(os.path.join(local_folder, filename), 'rb'), os.path.join(remote_folder, remote_name))
        self.words_api.upload_file(upload_request)

        request = asposewordscloud.models.requests.DeleteWatermarkRequest(remote_name, remote_folder)
        self.words_api.delete_watermark(request)

        # End README example
```

[Product Page](https://products.aspose.cloud/words/python) | [Documentation](https://docs.aspose.cloud/display/wordscloud/Home) | [API Reference](https://apireference.aspose.cloud/words/) | [Code Samples](https://github.com/aspose-words-cloud/Aspose.Words-Cloud-SDK-for-Python) | [Blog](https://blog.aspose.cloud/category/words/) | [Free Support](https://forum.aspose.cloud/c/words) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
