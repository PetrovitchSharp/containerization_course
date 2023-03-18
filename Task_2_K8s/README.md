## ЛР 1 /  K8s 

---

### Установка

---

Minikube успешно поднят внутри VirtualBox


![Start](img/1.png)

![VBox](img/2.png)

![Config](img/3.png)

---

### Postgres

---

![Create](img/4.png)

![Get](img/5.png)

![Describe](img/6.png)

---

💡 Вопрос: важен ли порядок выполнения этих манифестов? Почему?

Ответ: Порядок имеет значение, т.к deployment не поднимется из-за отсутствия configmap'а с нужными ему значениями переменных

![Deployment](img/ans.png)

---

### Nextcloud

---

![Create](img/7.png)

![Get & Logs](img/8.png)

---

### Tunneling

---

![Expose](img/9.png)

![Port Forward](img/10.png)

![Web 1](img/11.png)

![Web 2](img/12.png)

---

### Dashboard

---

![Dashboard](img/13.png)

![Dashboard Web](img/14.png)

-----

💡 Вопрос: что (и почему) произойдет, если отскейлить количество реплик postgres-deployment в 0, затем обратно в 1, после чего попробовать снова зайти на Nextcloud?

Ответ: Nextcloud упадет с ошибкой 500. Углубленное копание в логи показало начилие ошибки аутентификации на стороне postgres'а, что, вероятно, и является причиной internal server error.

![Error 500](img/ans3.png)

![PgLogs](img/ans2.png)

---


