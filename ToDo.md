**HR Agency ERP — ToDo.md**

- The agency creates the profile for the user.
- Comapny Employee can add opening in the panel.
- Candidate can edit his profile in the panel.
- Agency Employee have some permissions in the panel.

### Now:

- Change ID to be UUID (Chats, User, ...).
- Company Employee can add openings
- Candidate can edit only his profile

---

- and for the other users tabs, I want to be able to ONLY and ONly create the user. No need to show them there at all. We can always see users from the users tab. So there it would be better to have the create only.

- The ability for a candidate to apply for a position (external template no problem).
- The ability for a company to contact a candidate(external template no problem).
- The ability to attach file in the chat
- Make chats end to end encrypted.

USE API's AND REACT FOR THE FRONT END

#####

ماذا تضيف لتميّز المشروع أكثر:

🔹 Flags/Alerts

Admin يضيف Flags للمرشحين أو الشركات (VIP, Blacklist, ...).

🔹 Activity Log (Audit Trail)

كل تعديل، حذف، قبول، رفض → يُسجّل (من فعل ماذا ومتى).

يظهر في صفحة خاصة بالAdmin.

🔹 Tag System

Tags للمرشحين والشركات (Python, Remote, Senior).

تُمكِّنك من بناء فلترة قوية.

🔹 Custom Admin Actions

Ex: Archive old Applications → action مخصص في Admin.

🔹 Documents Management

رفع ملفات للمرشحين (CV, شهادات) → يظهر Inline بالAdmin.

🔹 Dynamic Reports Export

Admin يصدّر تقارير PDF/Excel بفلترة مخصصة.

🔹 Reminders System

Admin يحدد Reminder → Email يُرسل بعد 3 أيام (مثلاً للتذكير بالرد على مرشح).

🔹 Contact History

سجل التواصل لكل مرشح/شركة (Email, Phone Call, Meeting).

أفكار وميزات إضافية:
📝 إدارة الوظائف (Job Management)

وصف: إضافة وتعديل وحذف الوظائف الشاغرة من قبل الشركات أو المشرفين.
📊 نظام تتبع المتقدمين (Applicant Tracking System - ATS)

وصف: متابعة حالة المرشح لكل وظيفة (متقدم، تحت المراجعة، مقابلة، مقبول، مرفوض). هذا هو جوهر عمل أي وكالة توظيف.
📄 ملفات متقدمة للمرشحين والشركات (Advanced Profiles)

وصف: أضف حقولاً مهمة مثل المهارات، الخبرة، التعليم، ورفع السيرة الذاتية للمرشحين. وأضف الصناعة، حجم الشركة، ونبذة عنها للشركات.
🔍 بحث وتصفية متقدمة (Advanced Search & Filtering)

وصف: تطوير البحث في لوحة التحكم للبحث عن المرشحين حسب المهارات أو سنوات الخبرة، والبحث عن الوظائف حسب الموقع أو المجال.
🧾 الفواتير والمدفوعات (Invoicing & Billing)

وصف: نظام بسيط لإنشاء وإدارة الفواتير للشركات بعد عملية توظيف ناجحة.
📈 تقارير ولوحات معلومات (Reports & Dashboards)

وصف: صفحة في لوحة التحكم لعرض إحصائيات أساسية مثل: عدد المرشحين، عدد الشركات، والوظائف المفتوحة، وعدد التعيينات الناجحة شهرياً.
🗓️ جدولة المقابلات (Interview Scheduling)

وصف: أداة بسيطة للمشرفين لتحديد وتتبع مواعيد المقابلات بين المرشحين والشركات.
📋 ملاحظات وسجلات النشاط (Notes & Activity Logs)

وصف: إضافة قسم للملاحظات الداخلية على ملف كل مرشح أو شركة، وسجل لتتبع الإجراءات المهمة التي يقوم بها المشرفون.
++++++
امكانية سؤال البوت لكي يعطيني اشخاص او شركات للتعامل معها على حسب حاجتي

#####

# 1️⃣ General Structure

1.1 Users
Extend existing CustomUser model:

- position → CharField

- points → IntegerField (number of successful matches)

Permissions:

- Superuser → Full access.

Staff (is_staff=True):

- Can view only their own profile.

- Can view only their own chats and messages.

  1.2 Companies
  Create Company model:

- name

- address

- contact_info

- related_user → ForeignKey to User managing this company (optional).

  1.3 Candidates
  Create Candidate model:

- name

- cv → FileField or URLField

- email

- phone

- skills → TextField

- notes

related_user → ForeignKey to User who added the candidate.

1.4 Company Requests
Create CompanyRequest model:

company → ForeignKey

requested_position

requirements → TextField

status → Choices: open / closed / matched.

1.5 Matches
Create Match model:

company_request → ForeignKey

candidate → ForeignKey

matched_by → ForeignKey to User

match_date → DateTimeField

status → Choices: pending / approved / rejected.

1.6 Chats
Use existing Chat and Message models.

Restrict access:

Superuser → Can view all chats.

Staff → Can view only chats they are part of.

Company → Can view only their own chats.

Candidate → Can view only their own chats.

All users → Can access the ChatBot chat.

# 2️⃣ Backend Logic

2.1 Permissions & Validations
Implement model-level and view-level permission checks:

Staff cannot view other staff profiles.

Staff cannot view other staff chats or messages.

Company → Can access only their own profile and chats.

Candidate → Can access only their own profile and chats.

Create reusable permission logic:

is_owner_or_superuser method / mixin.

2.2 Admin Panel (Django Admin)
Superuser can manage in the Admin panel:

Users

Companies

Candidates

Company Requests

Matches

Chats & Messages

Add proper list_display, search_fields, and filters to admin classes.

Configure field permissions where needed (readonly / editable).

2.3 Views
Use only Django Admin for now (no REST API).

Generate basic templates with ChatGPT if needed (for the frontend).

3️⃣ Final Polish
3.1 Dashboard Pages (Admin panel)
Superuser Dashboard:

Global statistics (total users, total companies, total matches).

Staff Dashboard:

Personal points.

Matches made.

Companies they manage.

Company Dashboard:

Requests & Matches.

Candidate Dashboard:

Matches they are in.

Chats.

3.2 Extra Features
Auto-increment points when a staff user successfully matches a candidate.

Optional (for later): CV parsing feature → no Celery or Redis.

Basic audit log:

Who matched whom.

Who added what data.
